import urllib.request
import urllib.error
from socket import timeout
from xml.etree import ElementTree
import re

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from tqdm import tqdm

from packages.models import Package, Maintainer


class Command(BaseCommand):
    @staticmethod
    def handle(*args, **options):
        req = urllib.request.Request('https://pypi.org/rss/packages.xml')

        try:
            response = urllib.request.urlopen(req, timeout=10)
        except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)

            print('HTTPError: {}'.format(e.code))
        except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)

            print('URLError: {}'.format(e.reason))
        except timeout as e:
            print('TIMEOUT: {}'.format(e.reason))
        else:
            # HTTP 200

            xml = ElementTree.fromstring(response.read(1024 * 1024))  # 1 MB

            for elem in xml[0].findall('item'):  # xml[0] = 'channel'
                item = {item_field.tag: item_field.text for item_field in elem.findall('*')}

                item['guid'] = item['guid'].replace('https://pypi.org/project/', '')[:-1]

                del item['pubDate']

                try:
                    Package.objects.create(**item)  # can be also crete_or_update if we want update
                except IntegrityError:  # guid must be unique, so duplicate throw error
                    pass

        packages = tqdm(Package.objects.filter(author_name__isnull=True))

        for package in packages:
            packages.set_description(str(package))  # return __str__

            req = urllib.request.Request(f"https://pypi.org/project/{package.guid}/")

            try:
                response = urllib.request.urlopen(req, timeout=10)
            except urllib.error.HTTPError as e:
                # Return code error (e.g. 404, 501, ...)

                print('HTTPError: {}'.format(e.code))
            except urllib.error.URLError as e:
                # Not an HTTP-specific error (e.g. connection refused)

                print('URLError: {}'.format(e.reason))
            except timeout as e:
                print('TIMEOUT: {}'.format(e.reason))
            else:
                data = response.read(1024 * 1024).decode('utf-8')  # 1 MB, bytes => str

                update_data = {
                    'author_name': '-',  # ex: https://pypi.org/project/nbapy/ has no author
                    'author_email': None,
                }

                match = re.search(r"<strong>Author:</strong> (.*?)</p>", data)

                if match:
                    author = match.group(1)

                    update_data.update({
                        'author_name': author,
                    })

                    if 'a href' in author:
                        if 'mailto' in author:
                            match = re.match(r"<a href=\"mailto:(.*?)\">(.*?)</a>", author)

                            update_data.update({
                                'author_name': match.group(2),
                                'author_email': match.group(1),
                            })

                match = re.search(r", version (.*?)<", data)

                if match:
                    update_data.update({
                        'current_version': match.group(1),
                    })

                matches = re.findall(r"<a href=\"/user/.*?/\" aria-label=\"(.*?)\">", data)

                if matches:
                    for maintainer in set(matches):
                        try:
                            Maintainer.objects.create(**{
                                'package': package,
                                'name': maintainer,
                            })
                        except IntegrityError:
                            pass

                Package.objects.filter(pk=package.pk).update(**update_data)

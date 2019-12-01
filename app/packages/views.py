from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Package, Maintainer


def search(request):
    packages_all = Package.objects.all().order_by('title')

    q = request.GET.get('q')

    if q:
        packages_all = packages_all.filter(
            Q(guid__icontains=q)
            | Q(title__icontains=q)
            | Q(author_name__icontains=q)
            | Q(author_email__icontains=q)
            | Q(current_version__icontains=q)
            | Q(description__icontains=q)
        )

        packages_all = packages_all | Package.objects.filter(
            pk__in=[maintainer.package.pk for maintainer in Maintainer.objects.filter(name__icontains=q)]
        )

    paginator = Paginator(packages_all, settings.PER_PAGE)

    page = request.GET.get('page')
    packages = paginator.get_page(page)

    return render(request, 'packages/package/search.html', {
        'packages': packages,
        'url': f"/packages?q={q}&" if q else "/packages?",
    })

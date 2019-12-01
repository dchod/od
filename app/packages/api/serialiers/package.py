from rest_framework import serializers

from ...models import Package


class PackageListSerializer(serializers.ModelSerializer):
    maintainers = serializers.SerializerMethodField()

    class Meta:
        model = Package
        read_only_fields = fields = ('pk', 'guid', 'title', 'link', 'author_name', 'author_email', 'current_version',
                                     'description', 'maintainers')

    @staticmethod
    def get_maintainers(obj):
        return [maintainer.name for maintainer in obj.maintainer_set.all()]

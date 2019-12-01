from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from ..documents.package import PackageDocument


class PackageDocumentSerializer(DocumentSerializer):
    class Meta(object):
        document = PackageDocument
        fields = (
            'id',
            'guid',
            'title',
            'author_name',
            'author_email',
            'current_version',
            'description',
            'maintainers',
        )

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination

from ..documents.package import PackageDocument
from ..serializers.package import PackageDocumentSerializer


class PackageDocumentView(BaseDocumentViewSet):
    document = PackageDocument
    serializer_class = PackageDocumentSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    search_fields = (
        'guid',
        'title',
        'author_name',
        'author_email',
        'current_version',
        'description',
        'maintainers',
    )
    filter_fields = {
        'guid': 'guid.raw',
        'title': 'title.raw',
        'author_name': 'author_name.raw',
        'author_email': 'author_email.raw',
        'current_version': 'current_version.raw',
        'description': 'description.raw',
        'maintainers': {
            'field': 'maintainers',
        },
    }
    ordering_fields = {
        'id': 'id',
    }
    ordering = ('id', )

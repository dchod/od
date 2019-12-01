from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields

from packages.models import Package

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@INDEX.doc_type
class PackageDocument(Document):
    id = fields.IntegerField(attr='id')

    guid = fields.StringField(fields={
        'raw': fields.StringField(),
    })
    title = fields.StringField(fields={
        'raw': fields.StringField(),
    })
    author_name = fields.StringField(fields={
        'raw': fields.StringField(),
    })
    author_email = fields.StringField(fields={
        'raw': fields.StringField(),
    })
    current_version = fields.StringField(fields={
        'raw': fields.StringField(),
    })
    description = fields.StringField(fields={
        'raw': fields.StringField(),
    })
    maintainers = fields.StringField(
        attr='maintainers_indexing',
        fields={
            'raw': fields.StringField(multi=True),
        },
        multi=True
    )

    class Django(object):
        model = Package

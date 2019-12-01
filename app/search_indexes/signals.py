from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    app_label = sender._meta.app_label

    if app_label == 'package':
        registry.update(kwargs['instance'])


@receiver(post_delete)
def delete_document(sender, **kwargs):
    app_label = sender._meta.app_label

    if app_label == 'package':
        registry.update(kwargs['instance'])

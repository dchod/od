from django.db import models
from django.utils.translation import gettext as _


class Package(models.Model):
    guid = models.CharField(max_length=255, verbose_name=_("Nazwa"))
    title = models.CharField(max_length=255)
    link = models.URLField(verbose_name="URL")
    author_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Autor"))
    author_email = models.EmailField(null=True, blank=True, verbose_name=_("Email autora"))
    current_version = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Aktualna wersja"))
    description = models.TextField(verbose_name=_("Opis"))

    def __str__(self):
        return self.guid

    class Meta:
        verbose_name = _("Pakiet")
        verbose_name_plural = _("Pakiety")
        unique_together = ['guid']

    @property
    def maintainers_indexing(self):
        return [maintainer.name for maintainer in self.maintainer_set.all()]


class Maintainer(models.Model):
    package = models.ForeignKey(Package, verbose_name=_("Pakiet"), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_("zarządca"))

    def __str__(self):
        return f"{self.name} ({self.package})"

    class Meta:
        verbose_name = _("zarządca")
        verbose_name_plural = _("zarządcy")
        unique_together = ['package', 'name']

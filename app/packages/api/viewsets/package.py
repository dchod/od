from django.conf import settings
from django.db.models import Q

from rest_framework import pagination, viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from ...models import Package, Maintainer
from ..serialiers.package import PackageListSerializer


class DefaultResultsSetPagination(pagination.LimitOffsetPagination):
    default_limit = settings.PER_PAGE
    max_limit = 100


class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageListSerializer
    pagination_class = DefaultResultsSetPagination
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    def get_queryset(self):
        qs = Package.objects.all()

        q = self.request.GET('q')

        if q:
            qs = qs.filter(
                Q(guid__icontains=q)
                | Q(title__icontains=q)
                | Q(author_name__icontains=q)
                | Q(author_email__icontains=q)
                | Q(current_version__icontains=q)
                | Q(description__icontains=q)
            )

            qs = qs | Package.objects.filter(
                pk__in=[maintainer.package.pk for maintainer in Maintainer.objects.filter(name__icontains=q)]
            )

        return qs

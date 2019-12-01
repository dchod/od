from django.conf.urls import url, include

from rest_framework import routers

from .api.viewsets.package import PackageViewSet

router = routers.DefaultRouter()
router.register(r'package', PackageViewSet, 'package')

urlpatterns = [
    url(r'', include(router.urls)),
]

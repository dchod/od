from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .viewsets.package import PackageDocumentView

router = DefaultRouter()
packages = router.register(r'packages', PackageDocumentView, basename='packagedocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]

from django.urls import path, include

urlpatterns = [
    path('packages', include('packages.urls')),
    path('api/packages/', include('packages.urls_api')),

    path('search/', include('search_indexes.urls')),
]

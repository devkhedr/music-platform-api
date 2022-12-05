from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artists.urls')),
    path('', include('albums.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('authentication/', include('authentication.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

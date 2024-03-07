from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from users.views import CustomUserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('products.urls')),
    path('users/me/', CustomUserViewSet.as_view({'get': 'me'}), name='user-me'),
    path('users/me/update/', CustomUserViewSet.as_view({'put': 'update_profile'}), name='user-update-profile'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]

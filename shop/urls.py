from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
# from products.views import CustomTokenCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/auth/login/', CustomTokenCreateView.as_view(), name='token_create'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('products.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]

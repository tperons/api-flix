from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path('api/v1/authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/authenticarion/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path('__debug__', include(debug_toolbar.urls)), * urlpatterns]

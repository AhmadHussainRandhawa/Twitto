from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/twitto/', permanent=False), name='home'),  # Redirect root to /twitter/
    path('__reload__/', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),
    path('twitto/', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


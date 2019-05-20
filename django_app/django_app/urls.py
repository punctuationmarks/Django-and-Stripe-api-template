from django.contrib import admin
from django.urls import path, include

# imports for viewing images from the site ()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forSale.urls')),
]



# allowing images to be viewed during DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

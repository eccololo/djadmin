from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from education.admin import education_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education-admin/', education_site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from education.admin import education_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education-admin/', education_site.urls),
    path('captcha/', include('captcha.urls')),
    path('datawizard/', include('data_wizard.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

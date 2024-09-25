from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import upload_invoice

urlpatterns = [
    path('', upload_invoice, name='upload_invoice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.index),
    path('upload/', views.upload),
    path('bio/', views.bio),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
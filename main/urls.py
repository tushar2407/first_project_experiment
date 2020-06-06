from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.index),
    path('upload/', views.upload, name="upload"),
    path('books/',views.book_list, name="book_list"),
    path('books/upload/',views.book_upload, name="upload_book"),

    path("class/books/",views.BookListView.as_view(), name="class_book_list"),
    path("class/books/upload",views.UploadBookView.as_view(), name="class_book_upload"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
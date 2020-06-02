from django.urls import path
from account.views import registration_view
urlpatterns=[
    path('', registration_view),
]
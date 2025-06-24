from django.urls import path
from .views import PublicAPI, PrivateAPI

urlpatterns = [
    path('public/', PublicAPI.as_view(), name='public-api'),
    path('private/', PrivateAPI.as_view(), name='private-api'),
]

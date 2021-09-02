from django.contrib import admin
from django.urls import path
from .views import QR, QRDetail


urlpatterns = [
    path("add-product/", QR.as_view()),
    path("products/<str:pk>/", QRDetail.as_view()),
]

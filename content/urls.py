from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_cadet/", views.add_cadet, name='add_cadet'),
    path('cadet/<int:cadet_id>/', views.cadet_detail, name='cadet_detail'),
    path("shifts/", views.show_shifts, name='shifts')
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.ForSalePage, name="home"),
    path('charge_through_stripe/', views.charge_through_stripe, name="charge_sucessful"),
    path('charge_10_through_stripe/', views.charge_10_through_stripe, name="charge_10_sucessful")
]

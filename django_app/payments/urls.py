from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('charge_5_through_stripe/', views.charge_5_through_stripe, name="charge_5_sucessful"),
    path('charge_10_through_stripe/', views.charge_10_through_stripe, name="charge_10_sucessful")
]

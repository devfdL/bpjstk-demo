from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='payment'),
    path('paymentver', views.ver, name='paymentver'),
    path('paymentface', views.payface, name='paymentface'),
]
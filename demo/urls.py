from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path('',views.index, name='home'),
    path('userdata/', include('userData.urls'), name= 'userdata'),
    path('payment/', include('payment.urls'), name= 'payment'),
]

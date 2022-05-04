"""tiaozao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tiaozaoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="indexshop"),
    path('add/',views.add,name="addshop"),
    path('insert/',views.insert,name="insertshop"),
    path('addB/', views.addB, name="addBshop"),
    path('insertB/', views.insertB, name="insertBshop"),
    path('user_login/',views.login,name='loginshop'),
    path('user_dologin/',views.dologin,name='dologinshop'),
    path('aob/',views.aorb,name="aob"),
    path('user_Ainsert/',views.A,name='Ainsert'),
    path('user_Binsert/',views.B,name='Binsert'),
    path('vlogin/',views.v_login,name='vLogin'),
    path('dovlogin/',views.dovlogin,name='dovLogin'),
]

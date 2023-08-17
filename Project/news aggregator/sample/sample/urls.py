"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app1 import views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('hello/', views.show8),
    path('/home', views.show3),
    path('login/', views.show2),
    path('', views.topnews),
    path('contactus/', views.show4),
    path('blog/', views.show5),
    path('aboutus/', views.show6),
    path('signup/', views.show7),
    path('dashboardM/', views.show9),
    path('userdet/', views.adduser),
    path('insuser/', views.insuser),
    path('showusers/', views.showuser),
    path('edit/<int:id>', views.edit),
    path('update1/<int:id>', views.update1),
    path('delete/<int:id>', views.delete1),
    path('login2/', views.login2),
    path('logout/', views.logout),
    path('empform/', views.addempform),
    path('feedback', views.feedback),
    path('sports/', views.sports),
    path('worldnews/', views.worldnews),
    path('vadodaranews/', views.vadodaranews),
    path('ins_feedback/', views.ins_feedback),
    path('covid19/', views.covid19),
}

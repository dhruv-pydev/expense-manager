"""expense_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from main import urls as main_urls
from user_management import views as user_management_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', view=user_management_views.LoginView.as_view()),
    path('logout/', view=user_management_views.LogoutView.as_view()),
    path('api/v1/', include(main_urls.router.urls)),
]

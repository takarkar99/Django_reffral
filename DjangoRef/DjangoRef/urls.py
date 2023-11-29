"""
URL configuration for DjangoRef project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import main_view, SignUp, login_view, logout_view
from Profile.views import my_recommended_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_urls'),
    path('signup/', SignUp, name='signup_urls'),
    #path('<str:ref_code>/', main_view)
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('profile/', my_recommended_view, name='profile_url')
]
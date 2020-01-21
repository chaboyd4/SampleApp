"""SampleApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from sample_app import views # STEP 1 URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home, name= 'home'), # STEP 1) URL linking the three things together, views.home is the function
    path('^$', views.home, name='home') #don't need to run server again, so
]
# 3 STEPS: 1) URL, 2) Function, 3) Template
"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import handler400,handler404,handler403,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("GestionTareas.urls"))
]

handler400 = 'GestionTareas.views.mi_error_400'
handler403 = 'GestionTareas.views.mi_error_403'
handler404 = 'GestionTareas.views.mi_error_404'
handler500 = 'GestionTareas.views.mi_error_500'
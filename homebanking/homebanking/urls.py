"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views as login_views
from django.conf import settings
from django.conf.urls.static import static
from tarjetas import views as tarjetas_views
from prestamos import views as prestamo_views
<<<<<<< HEAD
from cuentas import views as cuentas_views
from django.urls import include
=======
from cuentas import views 
>>>>>>> a215a03f989bcc0da169dcc4aa5d89c3db3c803d


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.login, name="login"),
    path('tarjetas/', tarjetas_views.Tarjeta, name="tarjetas"),
    path('prestamos/', prestamo_views.prestamo, name="prestamos"),
<<<<<<< HEAD
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',login_views.registro, name="registro"),
=======
    path('cuentas/', views.Cuenta, name= "cuentas"),
>>>>>>> a215a03f989bcc0da169dcc4aa5d89c3db3c803d
]

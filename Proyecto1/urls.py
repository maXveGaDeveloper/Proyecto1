from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, otro_saludo, DiaDeHoy
from Proyecto1.views import probandoTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('otro_saludo/', otro_saludo),
    path('DiaDeHoy/', DiaDeHoy),
    path('probandoTemplate/', probandoTemplate),
]


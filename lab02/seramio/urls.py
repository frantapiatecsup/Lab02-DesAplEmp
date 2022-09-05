from django.urls import path

from . import views

app_name = 'cilindro'
app_name = 'calcular'
urlpatterns = [
    #ex: /encuesta/
    path('', views.vista, name='ejere1'),
    path('volumen', views.pops, name='ejere2'),
    path('resultado', views.ejer1, name='ejer1'),

    path('analizar', views.ejer2, name='ejer2'),
]


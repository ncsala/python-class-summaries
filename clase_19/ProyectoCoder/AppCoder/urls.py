from django.urls import path
from AppCoder.views import ver_curso, crear_curso, prueba_templates

urlpatterns = [
    path('ver/', ver_curso),
    path('crear/', crear_curso),
    path('template/', prueba_templates)
]

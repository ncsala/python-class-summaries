from django.urls import path
from AppCoder.views import ver_curso, crear_curso, prueba_templates, link1, link2, link3, link4

urlpatterns = [
    path('ver/', ver_curso),
    path('crear/', crear_curso),
    path('template/', prueba_templates),
    path('link1/', link1),
    path('link2/', link2),
    path('link3/', link3),
    path('link4/', link4),
]

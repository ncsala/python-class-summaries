from django.urls import path
from AppCoder.views import crear_curso, ver_curso

urlpatterns = [
    path('ver/', ver_curso),
    path('crear/', crear_curso),
]
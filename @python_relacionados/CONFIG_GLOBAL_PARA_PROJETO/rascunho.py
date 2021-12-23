

# from django.db import models
#
#     class Modelo(models.Model):
#         texto = models.CharField('Texto', max_length=500)
#
#         class Meta:
#             verbose_name = 'Texto'
#             verbose_name_plural = 'Textos'
#
#         def __str__(self):
#             return self.texto

# from django.contrib import admin
#     from .models import *
#
#     @admin.register(Modelo)
#     class ModeloAdmin(admin.ModelAdmin):
#         list_display = ('texto',)

# python manage.py makemigrations
# python manage.py migrate

# <!DOCTYPE html>
#     {% load bootstrap4 %}
#     {% load static %}
#     <html lang="en">
#     <head>
#         {% bootstrap_css %}
#         <link href="#" rel="stylesheet">
#         <meta charset="UTF-8">
#         <meta content="ie-edge" http-equiv="X-UA-Compatible">
#         <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
#         <title>Página</title>
#     </head>
#     <body>
#     {% bootstrap_javascript jquery='full' %}
#     </body>
#     </html>

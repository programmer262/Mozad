from django.contrib import admin
from .models import *


@admin.register(Cour)
class CourAdmin(admin.ModelAdmin):
     list_display = ['Professor','cour','partie','document']
     list_filter = ['cour','document']
     search_fields = ['cour','Professor']
admin.site.register(Matiére)
admin.site.register(Etudiant)
admin.site.register(Exercice)
admin.site.register(Corrigé)
admin.site.register(Classe)
admin.site.register(Live_ended)
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
     list_display = ['user','téléphone','email','Matiére']
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
      list_display = ['name']


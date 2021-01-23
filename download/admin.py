from django.contrib import admin
from .models import *

admin.site.register(Cour)
admin.site.register(Matiére)
admin.site.register(Etudiant)
admin.site.register(Exercice)
admin.site.register(Corrigé)
admin.site.register(Classe)
admin.site.register(Live_ended)
@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
     list_display = ['user','telephone','email','matiére']

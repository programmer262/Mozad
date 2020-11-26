from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Etudiant(models.Model): 
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=2000)
  téléphone = models.CharField(max_length=16)

  def __str__(self):
        return self.name
  
    
class Cour(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    document =models.TextField()
    cour = models.CharField(max_length=200)
    partie = models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.cour

    @property
    def docFILE(self):
           try:
               url = self.document.url
           except:
               url = ''
           return url


class Exercice(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.TextField()
    exercice = models.CharField(max_length=200)
    def __str__(self):
        return self.exercice
    @property
    def docFILE1(self):

           try:
               url = self.document.url
           except:
               url = ''
           return url

class Corrigé(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.TextField()
    correction_name = models.CharField(max_length=200)
    def __str__(self):
        return self.correction_name
    @property
    def docFILE2(self):
           try:
               url = self.document.url
           except:
               url = ''
           return url




class Classe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    lien = models.CharField(max_length=2000)
    matiére =  models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)
    date =  models.CharField(max_length=200)
    heure =  models.CharField(max_length=200)

    def __str__(self):
        return self.heure
class Live_ended (models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    matiére = models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)
    cour = models.CharField(max_length=100)
    partie = models.CharField(max_length=100)
    live = models.TextField()


    def __str__(self):
        return self.cour
    @property
    def docFILE3(self):
           try:
               url = self.live.url
           except:
               url = ''
           return url

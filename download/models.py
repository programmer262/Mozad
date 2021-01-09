from django.db import models
from django.contrib.auth.models import User

class Matiére(models.Model):
  matiére = models.CharField(max_length=2000)

  def __str__(self):
        return self.matiére
class Professor(models.Model): 
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.CharField(max_length=2000)
  téléphone = models.CharField(max_length=16)
  Matiére = models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
        return self.first_name + ' ' +self.last _name
  
class Etudiant(models.Model): 
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name  
  
    
class Cour(models.Model):
    Professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    document =models.FileField()
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
    Professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField()
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
    Professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField()
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
    Professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    lien = models.CharField(max_length=2000)
    type_of_language =  models.CharField(max_length=2000)
    date =  models.CharField(max_length=200)
    heure =  models.CharField(max_length=200)

    def __str__(self):
        return self.heure
class Live_ended (models.Model):
    Professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    matiére = models.CharField(max_length=2000)
    cour = models.CharField(max_length=100)
    partie = models.CharField(max_length=100)
    live = models.FileField()


    def __str__(self):
        return self.cour
    @property
    def docFILE3(self):
           try:
               url = self.live.url
           except:
               url = ''
           return url

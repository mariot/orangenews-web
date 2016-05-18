from django.db import models

# Create your models here.
class Depeche(models.Model):
    heure = models.DateTimeField()
    titre = models.CharField(max_length=50)
    contenu = models.TextField()

    class Meta:
    	ordering = ['heure']

    def __str__(self):
    	return self.titre

class Actualite(models.Model):
	CATEGORIES = (
        ('P', 'Politique'),
        ('S', 'Societe'),
        ('E', 'Economie'),
        ('C', 'Culture'),
        ('O', 'Sport'),
        ('I', 'Interview'),
        ('N', 'En image'),
        ('L', 'Lu pour vous'),
    )
	date = models.DateTimeField()
	titre = models.CharField(max_length=50)
	image = models.ImageField()
	categorie = models.CharField(max_length=3, choices=CATEGORIES)
	contenu = models.TextField()
	
	class Meta:
		ordering = ['date']

	def __str__(self):
		return self.titre
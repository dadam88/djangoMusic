from django.db import models

from authors.models import Author
# Create your models here.

class Song(models.Model):
	levels = ('one','one')
	author = models.ManyToManyField(Author)
	name = models.CharField(max_length=50, default="none")
	level = models.CharField(max_length=2, default=0)
	myfield = models.CharField(max_length=256, choices=[levels])
	
	def __unicode__(self):
		return self.name
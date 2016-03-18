from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
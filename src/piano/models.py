from django.db import models

# Create your models here.


class Song(models.Model):
	MUSIC_PERIODS = (
        ('B', 'Baroque'),
        ('C', 'Classical'),
        ('R', 'Romantic'),
        ('M', 'Modern'),
    )

	name		=	models.CharField(max_length=50)
	slug		=	models.SlugField(unique=True)
	composer	=	models.ForeignKey('Composer')
	books		=	models.ForeignKey('Book')
	level		=	models.CharField(max_length=1, default=0)
	period		=	models.CharField(max_length=20,
                                      choices=MUSIC_PERIODS,
                                      default='DEFAULT')

	def __unicode__(self):
		return self.name


class Composer(models.Model):
	name		=	models.CharField(max_length=50) 
	slug		=	models.SlugField(unique=True)

	def __unicode__(self):
			return self.name
			
class Book(models.Model):
	name		=	models.CharField(max_length=50)
	slug		=	models.SlugField(unique=True)
	publisher	=	models.CharField(max_length=50)

	def __unicode__(self):
		return self.name	


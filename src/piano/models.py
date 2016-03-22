from django.db import models

# Create your models here.


class Song(models.Model):
	MUSIC_PERIODS = (
        ('Baroque', 'Baroque'),
        ('Classical', 'Classical'),
        ('Romantic', 'Romantic'),
        ('Modern', 'Modern'),
    )

	LEVELS = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		('10', '10'),
		)

	name		=	models.CharField(max_length=50)
	slug		=	models.SlugField(unique=True, blank=True)
	composer	=	models.ForeignKey('Composer')
	books		=	models.ForeignKey('Book', default=1)
	level		=	models.CharField(max_length=2,
										choices=LEVELS, 
										default=1)
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


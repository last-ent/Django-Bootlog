from django.db import models

# Create your models here.

from django.http import HttpResponseRedirect

import datetime
from ckeditor.fields import RichTextField

class Blog(models.Model):
	blog = models.CharField(max_length = 50, blank = False)
	pub_date = models.DateField(default=datetime.datetime.now)

	def __unicode__(self):
		return "%s" %self.blog


class Category(models.Model):
	COLOUR_CHOICES=[
		 #('primary', 'Blue'),
		 ('default', 'Default'),
		 ('warning', 'Yellow'),
		 ('success', 'Green'),
		 ('info', 'Light Blue'),
		 ('danger', 'Red')
	]
	category = models.CharField(max_length=240,blank=False)
	colour = models.CharField(max_length=240,choices=COLOUR_CHOICES)

	def __unicode__(self):
		return "%s" %self.category

class Post(models.Model):
	title = models.CharField(max_length=240,blank=False, unique=True)
	entry = RichTextField()
	pub_date = models.DateField(default=datetime.datetime.now)
	category = models.ForeignKey(Category)
	blog = models.ForeignKey(Blog)
	publish = models.CharField(default="No", 
								max_length = 3, 
								choices=[("Yes", "Yes"),
										 ("No", "No")
										 ],
								)
	def get_absolute_url(self):
		return "/p/b%sp%s" %(self.blog.pk,self.pk)

	def __unicode__(self):
		return "%s" %self.title


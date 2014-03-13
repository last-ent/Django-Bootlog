from django.db import models

# Create your models here.
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
	title = models.CharField(max_length=240,blank=False)
	entry = RichTextField()
	pub_date = models.DateField(default=datetime.datetime.now)
	category = models.ForeignKey(Category)
	blog = models.ForeignKey(Blog)
	perma_link = models.CharField(max_length=50,blank = True)
	#colour = models.ForeignKey(Category.colour)

	# https://docs.djangoproject.com/en/1.6/topics/db/models/#overriding-model-methods
	def save(self, *args, **kwargs):
		super(Post,self).save(*args,**kwargs)
		if self.perma_link =='':
			self.perma_link = "b%sp%s" %(self.blog.pk,self.pk)
			self.save(*args, **kwargs)
			
	def __unicode__(self):
		return "%s" %self.title

class Comment(models.Model):
	comment = models.TextField(blank=False)
	handle = models.CharField(max_length=25, default="Anonymous")
	post = models.ForeignKey(Post)


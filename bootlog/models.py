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
		 ('primary', 'Blue'),
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
	#colour = models.ForeignKey(Category.colour)

	def __unicode__(self):
		return "%s" %self.title

# class Blog(models.Model):
# 	blogpost = models.ForeignKey(Post)
# 	blog_name=models.CharField(max_length=240,blank=False)




# colour = {
# 	'Red':'danger',
# 	'Light Blue':'info',
# 	'Blue':'primary',
# 	'Green':'success',
# 	'Default':'default',
# 	'Yellow':'warning',
# }

# printcolour
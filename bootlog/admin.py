from django.contrib import admin

# Register your models here.

from .models import Category, Post, Blog

class BlogAdmin(admin.ModelAdmin):
	list_display=['blog','pub_date']
	search_fields = ['blog']
	list_filter = ['blog','pub_date']
	fields = ['blog']

class PostAdmin(admin.ModelAdmin):
	list_display=('title','category','pub_date')
	search_fields=('title','category')
	list_filter=['category','pub_date']
	fieldsets=[
		(None, {'fields':['title','blog','category']}),
		('Blog Entry',{'fields':['entry']}),
#		('Date',{'fields':['pub_date'], 'classes':['collapse']}),
		]

class CategoryAdmin(admin.ModelAdmin):
	list_display=('category','colour')
	search_fields= ['category',]
	list_filter=['colour']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
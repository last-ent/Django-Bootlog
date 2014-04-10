from django.contrib import admin

# Register your models here.

from .models import Category, Post, Blog


class BlogAdmin(admin.ModelAdmin):
	list_display=['blog','pub_date']
	search_fields = ['blog']
	list_filter = ['blog','pub_date']
	fields = ['blog']

class PostAdmin(admin.ModelAdmin):
	list_display=('title','blog','category','pub_date', 'publish',)
	search_fields=('title','blog','category', 'publish')
	list_filter=['category','blog','pub_date', 'publish']
	fieldsets=[
		("Details", {'fields':['title','blog','category', 'publish','pub_date'], 'classes': ('grp-collapse grp-closed','collapse'),}),
		('Blog Entry',{'fields':['entry'], 'classes': ('grp-collapse grp-closed','collapse'),}),

		]

class CategoryAdmin(admin.ModelAdmin):
	list_display=('category','colour')
	search_fields= ['category',]
	list_filter=['colour']


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
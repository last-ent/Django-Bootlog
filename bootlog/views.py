from django.shortcuts import render, render_to_response
from django.http import HttpResponse
#from .models import Post
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from django.conf import settings

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

context_dict = {
	'header_title':'Welcome to Django Blog App',
	'header':'bootlog/head.html',
	'toprow':'bootlog/top_row.html',
	'tri_stack':'bootlog/tri_stack.html',
	'footer_row':'bootlog/footer_row.html',
	'banner':"Django Blog App ",
	'mid_column':"bootlog/mid_column.html",
	'side_panel':'bootlog/side_panel.html',
	'base_page': 'bootlog/base.html',
	'footer_caption': 'This site is powered by Django, Bootstrap & Glyphicons.',
	'post_single':'bootlog/post.html',
	'about_us_page' : 'bootlog/about_us.html',
	'series_html' : 'bootlog/series_html.html',
	'default_metadata' : "Django Bootlog powered Blog App",
	'jscript_html' : 'bootlog/jscript_html.html',

	'RSS' : {
		'title': 'Bootlog Latest Posts',
		'link': 'http://127.0.0.1:8000/' ,
		'description': "Updates and latest news about Django Bootlog",

	}
}

def write_context_dict(keys, c_d, s_c_d):
	for key in keys:
		c_d[key]= s_c_d[key]

if hasattr(settings,'BOOTLOG_CONTEXT_DICT'):
	setting_context_dict = settings.BOOTLOG_CONTEXT_DICT
	setting_context = setting_context_dict.keys()
	if len(setting_context) >1:
		raise(Exception("BOOTLOG_CONTEXT_DICT has more than one key! Only one can be present."))
	else:
		setting_context = setting_context.pop()
		keys = setting_context_dict[setting_context].keys()
		if setting_context == 'customize':
			write_context_dict(keys,context_dict, setting_context_dict)
		elif setting_context =='rewrite':
			context_dict = {}
			write_context_dict(keys,context_dict, setting_context_dict)
		else:
			raise(Exception("BOOTLOG_CONTEXT_DICT has a key: '%s'. Only 'rewrite' or 'custom' is acceptable." %setting_context))

if 'posts_per_page' not in context_dict.keys():
	context_dict['posts_per_page'] = 3 

posts_per_page= context_dict['posts_per_page']

def get_category_post_count(posts=False):
	if posts:
		categories =[p.category for p in  posts ]
		cat_dict={}
		for category in categories:
			cat_dict[category.category] = {
			'colour': category.colour, 
			'count' : posts.filter(category__category=category.category).aggregate( Count('title'))['title__count'],

			}
		return cat_dict
	else:
		return None

def get_paginated_view(rq,items,nos):
	items_paginated = False
	paginator = Paginator(items,nos)
	page = rq.GET.get('page')
	try:
		items_paginated = paginator.page(page)
	except PageNotAnInteger:
		items_paginated=paginator.page(1)
	except EmptyPage:
		items_paginated=paginator.page(paginator.num_pages)
	return items_paginated

class BSearchView(SearchView):
	def create_response(self):
		"""
		Generates the actual HttpResponse to send back to the user.
		"""
		(paginator, page) = self.build_page()

		context = {
			'query':self.query,
			'form':self.form,
			'page':page,
			'paginator':paginator,
			'suggestion':None,
		}
		entries = [result for result in page.object_list if Post.objects.get(pk=result.pk).publish=="Yes"]

		context_dict['category_split'] = get_category_post_count()
		context.update(context_dict)
		context['entries'] = entries 
		
		if self.results and hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
			context['suggestion'] = self.form.get_suggestion()
		
		return render_to_response(self.template, context, context_instance = self.context_class(self.request))


def perma_post(request,blog_pk,post_pk):
	entry = Post.objects.filter(blog=blog_pk,pk=post_pk)
	context_dict['entries'] = entry
	disqus_tag = hasattr(settings,'BOOTLOG_DISQUS_SHORTNAME')
	context_dict['disqus_tag'] = disqus_tag
	if disqus_tag:
		context_dict['DISQUS_SHORTNAME'] = settings.BOOTLOG_DISQUS_SHORTNAME
	return render(request,context_dict['base_page'],context_dict)

import logging
logger = logging.getLogger(__name__)
def view_404(request):
	context_dict['msg']='Why a 404!!!'
	context_dict['category_split'] = get_category_post_count()
	logger.error("Got a 404")
	logger.debug("Got a 404")
	logger.info("Got a 404")
	logger.warning("Got a 404")
	logger.critical("Got a 404")
	return render(request,'bootlog/404.html',context_dict)


class LatestEntriesFeed(Feed):
	title = context_dict['RSS']['title']
	link =  context_dict['RSS']['link']
	description =  context_dict['RSS']['description']

	def items(self):
		return Post.objects.order_by('-id')[:5]

	def item_title(self,item):
		return item.title

	def item_description(self, item):
		s = item.entry[:150]
		if s[-1] == '.':
			s = s[:-1]
		return "%s..." %s

	def item_link(self,item):
		return reverse('blog-post',args=[item.blog.pk,item.pk])

def pre_html_render(request, entries, posts):
	context_dict['entries'] = get_paginated_view(request,entries,posts_per_page)
	context_dict['category_split'] = get_category_post_count(posts)
	context_dict['disqus_tag'] = False
	return render(request,context_dict['base_page'],context_dict)

def html_render(request,blog_name=None):
	posts = Post.objects.filter(blog__blog=blog_name) if blog_name else Post.objects.all()
	posts = posts.exclude(publish="No")
	non_cat_posts = posts
	category = request.GET.get('category')
	if category:
		posts = Post.objects.filter(category__category=category)
	entries = posts.order_by('-pub_date')
	return pre_html_render(request, entries, non_cat_posts)

def front_page_view(request):
	posts = Post.objects.exclude(blog__blog="About Us").exclude(publish="No")
	entries = posts.order_by('-pub_date')[:6]
	context_dict['metadata'] = context_dict['default_metadata']
	return pre_html_render(request, entries, posts)


def view_function_factory(bname, metadata=False):
	
	def ret_func(request):
		context_dict['metadata'] = metadata if metadata else context_dict['default_metadata']
		return html_render(request, blog_name=bname)

	return ret_func

class BlogSitemap(Sitemap):
	changefreq="weekly"
	priority = 0.5

	def items(self):
		return Post.objects.exclude(publish="No")

	def lastmod(self,obj):
		return obj.pub_date

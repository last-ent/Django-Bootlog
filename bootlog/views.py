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

from .forms import CommentForm

context_dict = {
	'header_title':'Welcome to Django Blog App',
	'header':'bootlog/head.html',
	'toprow':'bootlog/top_row.html',
	'tri_stack':'bootlog/tri_stack.html',
	'footer_row':'bootlog/footer_row.html',
	'extra_layout':True,
	'banner':"Django Blog App ",
	"echo": "This is Tron!",
	'mid_column':"bootlog/mid_column.html",
	'side_panel':'bootlog/side_panel.html',
	'base_page': 'bootlog/base.html',
	'footer_caption': 'This site is powered by Django, Bootstrap & Glyphicons.',
	'post_single':'bootlog/post.html',
	'url_addr': '127.0.0.1:8000/b/',
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
		#dict_keys = context_dict.keys()
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

def get_category_post_count():
	categories = Category.objects.all()
	cat_dict={}
	for category in categories:
		cat_dict[category.category] = {
		'colour': category.colour, 
		'count':Post.objects.filter(category__category=category.category).aggregate(
													Count('title'))['title__count'],
		}
	return cat_dict

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


def home(request):
	if not request.GET.get('category'):
		posts = Post.objects.all()
	else:
		posts = Post.objects.filter(category__category=request.GET.get('category'))
	entries = posts.order_by('-id')
	context_dict['entries'] = get_paginated_view(request,entries,posts_per_page)
	context_dict['category_split'] = get_category_post_count()
	return render(request,context_dict['base_page'],context_dict)

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
		context_dict['category_split'] = get_category_post_count()
		context.update(context_dict)
		context['entries'] = [result for result in page.object_list]
		
		if self.results and hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
			context['suggestion'] = self.form.get_suggestion()
		
		return render_to_response(self.template, context, context_instance = self.context_class(self.request))

def perma_post(request,blog_pk,post_pk):
	entry = Post.objects.filter(blog=blog_pk,pk=post_pk)
	context_dict['entries'] = entry
	return render(request,context_dict['base_page'],context_dict)


def view_404(request):
	context_dict['mid_column'] = 'bootlog/404.html'
	context_dict['msg']='Why a 404!!!'
	context_dict['category_split'] = get_category_post_count()
	return render(request,context_dict['base_page'],context_dict)

def comment_view(request):
	if request.method == 'POST':

		form = CommentForm(request.POST)
		if form.is_valid():

			return HttpResponse("%s" %(form.cleaned_data))
		else:
			return HttpResponse(":-/")
	elif request.method == "GET":
		form = CommentForm()
		#return render(request, 'bootlog/form.html',{'form':form})
		context_dict['form'] = form
		
		return render(request, 'bootlog/comment_form.html',context_dict)
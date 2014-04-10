from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory
#from django.contrib import admin
#admin.autodiscover()
from . import views as bviews
from .views import BSearchView

urlpatterns = patterns('',
    
    url(r'^$',bviews.front_page_view),
    url(r'^s/',search_view_factory(
        view_class = BSearchView,
        template = 'bootlog/base.html',
        searchqueryset=SearchQuerySet(),
        form_class=ModelSearchForm
        ), name='haystack_search'),
    url(r'^d/', bviews.view_function_factory("Programming"), name='programming'),
    url(r'^s/',search_view_factory(
        view_class=BSearchView,
        template='bootlog/base.html',
        searchqueryset = SearchQuerySet(),
        form_class=ModelSearchForm
        ), name='haystack_search'),
    url(r'^about/$',bviews.view_function_factory("About Us")),
    url(r'^ckeditor/',include('ckeditor.urls')),
    url(r'^rss/$', bviews.LatestEntriesFeed(), ),
    url(r'^all/',bviews.html_render),
    url(r'^p/b(?P<blog_pk>\d+)p(?P<post_pk>\d+)/', bviews.perma_post, name="blog-post"),
    url(r'^sitemap\.xml$','django.contrib.sitemaps.views.sitemap',{'sitemaps': {'site': bviews.BlogSitemap}}),
)

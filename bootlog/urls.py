from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory
#from django.contrib import admin
#admin.autodiscover()
from . import views as bviews
from .views import BSearchView

urlpatterns = patterns('',
    
    url(r'^$',bviews.home),
    url(r'^s/',search_view_factory(
    	view_class = BSearchView,
    	template = 'bootlog/base.html',
    	searchqueryset=SearchQuerySet(),
    	form_class=ModelSearchForm
    	), name='haystack_search'),
    #url(r'^b/',include('bootlog.urls')),

 #   url(r'^admin/', include(admin.site.urls)),
)

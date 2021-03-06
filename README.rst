===============
Django Boot Log
===============

Django BootLog is a Django Blogging App based on Twitter Bootstrap theme. It allows the developers to make blog posts where the focus is on providing quick and acceptable blogging platform. 

Features
---------

* RTF Blog Posts
* Categories
* Search (Sidebar)
* Categorical Posts Listing
* Permalink
* Social Share - Reddit, Twitter, Google Plus, Facebook
* RSS Feed
* Multiple Blogs
* Draft Feature
* Comments Section
* Sitemap

Update
-------
I consider Django Bootlog to have reached a stable release - v 1.0; 
I have a site, entworks.in, where I will be journaling how I created the app.

Quick start
-----------

1. Add "bootlog" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'bootlog', # pip install django-bootlog
      )

2. You need to include following packages (dependencies)::

      INSTALLED_APPS = (
          ...
          'haystack', # pip install django-haystack
          'ckeditor', # pip install django-ckeditor-updated -- for Django >= 1.6
                      # pip install django-ckeditor         -- for Django <  1.6
      )

3. Following are some default settings used. You may change them as required::

		STATIC_URL = '/static/'

		HAYSTACK_CONNECTIONS = {
		    'default': { 
		        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine', # If Whoosh is used,
		                                                                   #     pip install whoosh
		        'PATH': os.path.join(BASE_DIR,'bootlog/whoosh_index'),
		    }
		}

		STATIC_ROOT=os.path.join(BASE_DIR, 'bootlog/STATIC_ROOT/')
		MEDIA_ROOT = os.path.join(BASE_DIR,'bootlog/media/')

		CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT,'/uploads/')
		CKEDITOR_CONFIGS = {
		           'default': {
		               'toolbar': 'Complete', # Other Option is 'Full'
		               'height': 300,
		               'width': 0, # Full Width
		           },
		       }

4. Include following urls in your project's URLconf::

      url(r'^blog/', include('bootlog.urls')), #The urls in the html for Top Bar have been written for '^/' url, you might need to change the href.
      url(r'^ckeditor/',include('ckeditor.urls')),
      url(r'^s/',search_view_factory(
        view_class = BSearchView,
        template = 'bootlog/base.html',
        searchqueryset=SearchQuerySet(),
        form_class=ModelSearchForm
        ), name='haystack_search'),
      url(r'^admin/',include(admin.site.urls)),

5. Run `python manage.py syncdb` to create the bootlog models, if you are using the app for the first time. Else you will have to migrate using south.

6. If you want to enable comments section, you will need to create a Disqus Admin account and include Disqus Shortname in your settings.py 
        BOOTLOG_DISQUS_SHORTNAME = <Disqus Site Shortname>

7. The default blog provided with the system is '/programming/'. If you wish to enable more blogs, it is a two step process:
        * In project/urls.py, add following line to urlpatterns:
            url(r'^new_blog_link', 'bootlog.views.view_function_factory("blog title or name", "metadata")),
        * Go to Admin account and create the new blog with the same "blog title or name"

8. Now you can write and store blog posts as drafts instead of publishing them.

9. The blog's sitemap can be found at `blog/sitemap.xml`

10. Start the development server and visit http://127.0.0.1:8000/admin/
   to create Posts (you'll need the Admin app enabled).

11. Run `python manage.py rebuild_index` to create the search index.

12. Visit http://127.0.0.1:8000/ to view your posts.

13. To customize the app from default settings, use the following options::

		BOOTLOG_CONTEXT_DICT = { # Include only one of the following two. 
		    'rewrite': {
			    # Use this option if you wish to change all the settings
		    },
		    'customize': {
			    # Use this option if only a few of the settings are to be changed
		    }
		}

Following are the default values::

		context_dict = {
			'header_title':'EntWorks - Engineering, Programming',
			'header':'bootlog/head.html',
			'toprow':'bootlog/top_row.html',
			'tri_stack':'bootlog/tri_stack.html',
			'footer_row':'bootlog/footer_row.html',
			'banner':"Django Blog App",
			'mid_column':"bootlog/mid_column.html",
			'side_panel':'bootlog/side_panel.html',
			'left_sidebar': 'bootlog/left_sidebar.html',
			'base_page': 'bootlog/base.html',
			'footer_caption': 'This Site is powered by Django, Twitter Bootstrap & Glyphicons.',
			'post_single':'bootlog/post.html',

			'about_us_page' : 'bootlog/about_us.html',
			'metadata' : "A Django Bootlog powered website",

			'RSS' : {
				'title': 'Entworks Latest Posts',
				'link': '127.0.0.1/',
				'description': "Updates and latest news from Entworks",

				}
			}


14. The App was developed with following environment::

		Django==1.6.2
		Whoosh==2.6.0
		argparse==1.2.1
		django-ckeditor-updated==4.2.7
		django-debug-toolbar==1.0.1
		django-haystack==2.1.0
		sqlparse==0.1.11
		wsgiref==0.1.2

I would appreciate any suggestions or comments you might have upon using it. Please email me at last_ent@outlook.com
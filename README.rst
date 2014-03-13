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

      url(r'^blog/', include('bootlog.urls')),
      url(r'^ckeditor/',include('ckeditor.urls')),

5. Run `python manage.py syncdb` to create the bootlog models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create Posts (you'll need the Admin app enabled).

7. Run `python manage.py rebuild_index` to create the search index.

8. Visit http://127.0.0.1:8000/blog/ to view your posts.

9. To customize the app from default settings, use the following options::

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
			'header_title':'Welcome to Django Blog App',
			'header':'bootlog/head.html',
			'toprow':'bootlog/top_row.html',
			'tri_stack':'bootlog/tri_stack.html',
			'footer_row':'bootlog/footer_row.html',
			'extra_layout':True,
			'banner':"Django Blog App ",
			"echo": "",
			'mid_column':"bootlog/mid_column.html",
			'side_panel':'bootlog/side_panel.html',
			'base_page': 'bootlog/base.html',
			'footer_caption': 'This site is powered by Django & Bootstrap',
			'post_single':'bootlog/post.html',
			'url_addr': '127.0.0.1:8000/b/',
		}

10. The App was developed with following environment::

		Django==1.6.2
		Whoosh==2.6.0
		argparse==1.2.1
		django-ckeditor-updated==4.2.7
		django-debug-toolbar==1.0.1
		django-haystack==2.1.0
		sqlparse==0.1.11
		wsgiref==0.1.2

I would appreciate any suggestions or comments you might have upon using it. Please email me at last_ent@outlook.com
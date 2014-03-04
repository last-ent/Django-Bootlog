================
Django Boot Log
================

Django BootLog is a Django Blogging App based on Twitter Bootstrap theme. It allows the developers to make blog posts where the focus is on providing quick and acceptable blogging platform. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_bootlog" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'bootlog',
      )

2. You might need to add additional dependencies::

      INSTALLED_APPS = (
          ...
          'haystack',
          'ckeditor',
      )

3. Following are some default settings used. You may change them as required::

		STATIC_URL = '/static/'

		HAYSTACK_CONNECTIONS = {
		    'default': { 
		        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine', #IF WHOOSH IS USED
		        'PATH': os.path.join(BASE_DIR,'bootlog/whoosh_index'),
		    }
		}

		STATIC_ROOT=os.path.join(BASE_DIR,'bootlog/STATIC_ROOT/')
		MEDIA_ROOT = os.path.join(BASE_DIR,'bootlog/media/')
		CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT,'/uploads/')
		CKEDITOR_CONFIGS = {
		    'default': {
		        'toolbar': 'Complete',
		        'height': 300,
		        'width': 0,
		    },
		}

4. Include the django-bootlog URLconf in your project urls.py like this::

      url(r'^blog/', include('bootlog.urls')),
      url(r'^ckeditor/',include('ckeditor.urls')),

5. Run `python manage.py syncdb` to create the django_bootlog models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create Posts (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/blog/ to view your posts.

8. To customize the app from default settings, use the following options::

		BOOTLOG_CONTEXT_DICT = {
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
		}
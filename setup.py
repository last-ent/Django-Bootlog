import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
	name='django-bootlog',
	version='1.0.1',
	packages=['bootlog'],
	include_package_data=True,
	license='New BSD License',
	description="A Django Blogging App based on Twitter Bootstrap Theme",
	long_description=README,
	url='entworks.in',
	author="Ent",
	author_email="last_ent@outlook.com",
	classifiers=[
		'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

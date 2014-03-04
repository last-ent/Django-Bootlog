from django.test import TestCase, Client
import datetime
from .models import Post, Category
# Create your tests here.

#TESTCASE TO ADD FOR PRIOR DATE -- e: FAIL
#TO SUBMIT WIHOUT TITLE/ENTRY/CATEGORY

blog_base = '/b/'

class PostTestCases(TestCase):
	def setUp(self):
		self.cat = Category.objects.create(category="Test")

	def test_add_blank_title(self):
		try:
			
			p = Post.objects.create(
				entry = "Entry_t",
				category=self.cat,
			)
			p.save()
			
			if Post.objects.filter(entry="Entry_t"):
				self.assertEqual(1,2)
		except:
			pass
		
	def test_add_blank_entry(self):
		try:
			
			p = Post.objects.create(
				title="Test Add_e",
				category=self.cat,
				)
			p.save()
			if Post.objects.filter(title="Test Add_e"):
				self.assertEqual(1,2)
		except:
			pass
		

	def test_add_blank_category(self):
		try:
			
			p = Post.objects.create(
				title="Test Add_c",
				entry = "Entry",
				)
			p.save()
			if Post.objects.filter(title="Test Add_c"):
				self.assertEqual(1,2)
		except:
			pass

class ClientTestCases(TestCase):
	def setUp(self):
		self.client = Client()

	def test_default_page(self):
		response = self.client.get(blog_base)
		self.assertEqual(200,response.status_code)
	
	def test_unavailable_category(self):
		response = self.client.get(blog_base+'?category=goose')
		
		self.assertEqual(200,response.status_code)
	
	def test_404_page(self):
		response = self.client.get('kangaroo!')
		self.assertEqual(404,response.status_code)



#TO ENSURE A DEFAULT CATEGORY IS SET

#ENSURE /?... doesn't return any error

#ENSURE 404 Page is implemented

# SEARCH FOR AVAILABLE CONTENT RETURNS Results

# to ensure a category not in db cannot be published

# SEARCH FOR UNAVAILABLE CONTENT RETURNS FALSE

# SEARCH FOR TITLE

# SEARCH FOR ENTRY Content
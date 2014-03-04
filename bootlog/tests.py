from django.test import TestCase
import datetime
from .models import Post, Category
# Create your tests here.

# class GetPage(TestCase):
# 	def test_index(self):
# 		resp = self.client.get('/b/')
# 		self.assertEqual(resp.status_code,200)

#TESTCASE TO ADD FOR PRIOR DATE -- e: FAIL
class AddEntry(TestCase):
	def test_add_blank_title(self):
		#print c
		try:
			c = Category.objects.create(category="Test")
			p = Post.objects.create(
				#title="Test Add",
				entry = "Entry",
				category=c,
			#	pub_date=datetime.datetime.now()-datetime.timedelta(days =2)
				)
			p.save()
			print "****&&&&&&&&&&-----------", Post.objects.filter(entry="Entry")
			if Post.objects.filter(entry="Entry"):
				self.assertEqual(1,2)
		except:
			pass
		
	def rtest_add_blank_entry(self):
		#print c
		try:
			c = Category.objects.create(category="Test")
			p = Post.objects.create(
				title="Test Add",
				#entry = "Entry",
				category=c,
			#	pub_date=datetime.datetime.now()-datetime.timedelta(days =2)
				)
			p.save()
		except:
			pass
		if Post.objects.filter(title="Test Add"):
			self.assertEqual(1,2)

	def ttest_add_blank_category(self):
		#print c
		try:
			c = Category.objects.create(category="Test")
			p = Post.objects.create(
				title="Test Add",
				entry = "Entry",
			#	category=c,
			#	pub_date=datetime.datetime.now()-datetime.timedelta(days =2)
				)
			p.save()
		except:
			pass
		if Post.objects.filter(title="Test Add"):
			self.assertEqual(1,2)

#TO SUBMIT WIHOUT TITLE/ENTRY/CATEGORY

#TO ENSURE A DEFAULT CATEGORY IS SET

#ENSURE /?... doesn't return any error

#ENSURE 404 Page is implemented

# SEARCH FOR AVAILABLE CONTENT RETURNS Results

# to ensure a category not in db cannot be published

# SEARCH FOR UNAVAILABLE CONTENT RETURNS FALSE

# SEARCH FOR TITLE

# SEARCH FOR ENTRY Content
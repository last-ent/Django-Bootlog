import datetime
from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	entry = indexes.CharField(model_attr='entry')
	category = indexes.CharField(model_attr='category')
	colour = indexes.CharField(model_attr='category__colour')
	pub_date = indexes.CharField(model_attr='pub_date')

	def get_model(self):
		return Post

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


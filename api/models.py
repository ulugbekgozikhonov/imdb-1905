from django.db import models


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class StreamPlatform(BaseModel):
	name = models.CharField(max_length=100)
	about = models.TextField()
	website = models.URLField()

	def __str__(self):
		return self.name


class WatchList(BaseModel):
	title = models.CharField(max_length=100)
	description = models.TextField()
	year = models.PositiveIntegerField()
	rating = models.FloatField()
	rating_count = models.PositiveIntegerField(default=0)
	stream = models.ForeignKey(StreamPlatform, on_delete=models.PROTECT,
	                           null=True, related_name='watchlist')

	def __str__(self):
		return self.title


class Review(BaseModel):
	description = models.TextField()
	rating = models.PositiveIntegerField(default=0)
	active = models.BooleanField(default=True)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE,
	                         null=True, related_name='reviews')
	watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE,
	                              null=True, related_name='reviews')

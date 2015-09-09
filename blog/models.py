from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length = 50)
	url = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "categories"
	
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	category = models.ForeignKey('Category', default = None)
	thumbnails = models.CharField(max_length = 200, null = True, default = None)
	created_date = models.DateTimeField(blank = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Menu(models.Model):
	label = models.CharField(max_length = 50)
	url = models.CharField(max_length = 200)
	position = models.IntegerField(default = 0)
	image = models.CharField(max_length = 200, default = 0)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
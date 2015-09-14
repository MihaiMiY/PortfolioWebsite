from django.db import models

class Settings(models.Model):
	title = models.CharField(max_length = 200)
	slug = models.CharField(max_length = 100, default = None)
	description = models.CharField(max_length = 500)

	class Meta:
		verbose_name_plural = "settings"

class Sidebar(models.Model):
	label = models.CharField(max_length = 200)
	url = models.CharField(max_length = 200)
	image = models.CharField(max_length = 200, blank = True)
	position = models.IntegerField(default = 1)

	class Meta:
		verbose_name_plural = "sidebar"


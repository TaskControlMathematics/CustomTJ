from django.db import models
from django.contrib.auth.models import User



class Categories(models.Model):
	category = models.CharField(max_length=64)

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self):
		return self.category

class Article(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField()
	date = models.DateField()
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"


class Task(models.Model):
	CHOISES = (
		('assigned','assigned'),
		('work','work'),
		('done','done')
	)
	title = models.CharField(max_length=128)
	text = models.TextField()
	date = models.DateField()
	user_from = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="user_from")
	status = models.CharField(max_length=128,choices=CHOISES)
	user_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,related_name="user_to")
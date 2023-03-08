from django.db import models

# Create your models here.
class TodoList(models.Model):
	task = models.CharField(max_length=18)
	description = models.TextField(max_length=100)
	time = models.TimeField(auto_now_add=True)

	class Meta:
		ordering = ["-id"]
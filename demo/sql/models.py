from django.db import models

class Exam(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	exams = models.ManyToManyField(Exam)
	age = models.IntegerField()

	def __str__(self):
		return self.name + " " + str(self.age) + " " + str(self.exams.all())

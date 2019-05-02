from django.db import models

# Create your models here.

class Employee(models.Model):
	eid = models.CharField(max_length=20)
	ename = models.CharField(max_length=100)
	eemail = models.EmailField()
	econtact = models.CharField(max_length=15)
	class Meta:
		db_table = "employee"


class Emplo(models.Model):
	eemail = models.EmailField()
	econtact = models.CharField(max_length=15)
	class Meta:
		db_table = "Emplo"

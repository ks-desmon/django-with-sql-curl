from django import forms
from crudapplication.models import *


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"

class EmployeeForm2nd(forms.ModelForm):
	class Meta:
		model = Emplo
		fields = ("econtact",)
from django.shortcuts import render , redirect

from crudapplication.forms import EmployeeForm ,EmployeeForm2nd

from crudapplication.models import Employee



def emp(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		form2 = EmployeeForm2nd(request.POST)
		if form.is_valid():
			try:
				form.save()
				form2.save()
				return redirect()
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request,"index.html",{"form":form})

def show(request):
	employees = Employee.objects.all()
	return render(request,"show.html",{"employee":employees})

def edit(request, id):
	employee = Employee.objects.get(id=id)
	return render(request,"edit.html",{'employee':employee})

def update(request,id):
	employee = Employee.objects.get(id=id)
	forms = EmployeeForm(request.POST, instance=employee)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,'edit.html',{'employee':employee})

def delete(request,id):
	employee=Employee.objects.get(id=id)
	return redirect('/show')
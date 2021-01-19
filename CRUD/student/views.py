from django.shortcuts import render,redirect
from .models import Student


# Create your views here.
def index(request):
    if request.method == "GET":
        student = Student.objects.all()
        context = {
            'students': student
        }
        return render(request,'student/index.html',context)

    elif request.method == "POST":
        #Receive Data from Form
        name = request.POST['full_name']
        varsity_id = request.POST['varsity_id']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']

        #Draf data
        fill_data = {
            'name': name,
            'varsity_id': varsity_id,
            'phone' : phone,
            'address' : address,
            'email' : email
        }

        #Form Validation
        error_msg = None
        if not name:
            error_msg = "Name is required"
        elif len(name)<4:
            error_msg = "Name must be at least 4 character."
        elif not varsity_id:
            error_msg = "Varsity ID is required"
        elif not phone:
            error_msg = "Phone is Required"
        elif not address:
            error_msg = "Address is Required"
        elif not email:
            error_msg = "Email is Required"
        elif Student.objects.filter(email=email):
            error_msg = "This Email already exists"
        elif Student.objects.filter(varsity_id=varsity_id):
            error_msg = "This Varsity ID already exists"




        if error_msg:
            student = Student.objects.all()
            data = {
                'error_msg' : error_msg,
                'students': student,
                'values': fill_data,
            }
            return render(request,'student/index.html',data)
        else:
            Student.objects.create(name=name, varsity_id=varsity_id,phone=phone,address=address,email=email)
            return redirect('/')


def action_handler(request,action, id):
    if action=='delete':
        student=Student.objects.get(id=id)
        student.delete()

    elif action == 'edit':
        if request.method=="GET":
            student = Student.objects.get(id=id)
            context = {
                'student': student
            }
            return render(request,'student/edit.html',context)

        elif request.method=="POST":
            name = request.POST['full_name']
            varsity_id = request.POST['varsity_id']
            phone = request.POST['phone']
            address = request.POST['address']
            email = request.POST['email']

            student = Student.objects.get(id=id)

            student.name = name
            student.varsity_id = varsity_id
            student.phone = phone
            student.address = address
            student.email = email

            student.save()

    return redirect('home')
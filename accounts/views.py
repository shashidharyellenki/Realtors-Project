from email import message
from django.shortcuts import redirect, render
from django.contrib import messages, auth
# Create your views here.
from listings.models import Listing #small testing purspose imported this
from django.contrib.auth.models import User #this is an inbuilt model in the django
# from django.contrib.auth import aut
'''
User model contains basic fields like email username firstname lastname passowrd and manymore
'''
from contacts.models import Contact #importing the contact model from contact app for dashboard

def register(request):
    if request.method == 'POST':
        #getting all the form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #checking both passwords
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already existed in the database')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already is in use')
                    return redirect('register')
                else:
                    #looks everything is fine... Now we will register the user into database
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    #to login after register we use the below line code
                    # auth.login(request, user)
                    user.save()
                    #sending a sucess message
                    messages.success(request,"You are registerd sucessfully")
                    return redirect('login')

        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render(request, './accounts/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST ['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect details')
            return redirect('login')
    else:
        return render(request, './accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out sucessfully')
        return redirect('index')
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts
    }
    return render(request, './accounts/dashboard.html',context)

from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
# from .models import objects
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# from appdj.user.models import User
from .forms import UserForm

# Create your views here.
def home(request):
    return HttpResponse(request, 'register.html')

def signup(request):
    if request.method == "POST":
        # print("POST request received")
        # print("Request POST data:", request.POST)
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            # print("Form is valid")
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create the user
            user = form.save(commit=False)
            user.firstname = firstname
            user.lastname = lastname
            user.username = username
            user.email = email
            user.password = password
            user.save()
            
            print("User created:", user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect('signin')
    else:
        form = UserForm()
    return render(request, 'sign_up.html', {'form': form})

    

def signin(request):
    return render(request,'sign_in.html')#, {'form':form})

def signout(request):
    return render(request,'sign_out.html')#, {'form':form})


from django.shortcuts import render, redirect
from django.http import HttpResponse #to return direct html code
from django.contrib.auth.models import User, auth
from .models import Features
from django.contrib import messages

# Create your views here.
#for feature
def index(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})

#wordcounter
def word_counter(request):
    return render(request,'word_counter.html')

#wordcounter
def counter(request):
    text = request.POST["text"]
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {"word_count": amount_of_words})

#creating a sign up page
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password did not match")
            return redirect('register')
    else:    
        return render(request,'register.html')
    
#login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect ('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request,'post.html',{'pk': pk })

def poster(request):
    posts = [1,2,3,'tim','tom','jhon']
    return render(request, 'poster.html', {'posts': posts})

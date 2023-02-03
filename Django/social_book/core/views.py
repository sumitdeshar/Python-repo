from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_mode

User = get_user_mode
# Create your views here.
def index(request):
    user =  User
    return render(request, 'index.html', {'user': user})
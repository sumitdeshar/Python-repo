from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST': 
        city = request.POST['city']
    return render(request, 'index.html',{'city':city})
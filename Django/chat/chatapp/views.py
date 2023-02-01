from django.shortcuts import render, redirect
from chatapp.models import Room, Message 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username) #redirecting the user to the existing room and passing the username with it
    else:
        new_room = Room.objects.create(name=room)   #creating the room to redirect the user if room doesnot exist
        new_room.save()
        return redirect('/'+room+'/?username='+username) 
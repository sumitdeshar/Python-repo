from django.shortcuts import render, redirect
from chatapp.models import *
from chatapp.forms import *
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import now 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name= room)
    return render(request, 'room.html',{
            'username': username,
            'room': room,
            'room_details': room_details  
            })

def checkview(request):
    # room = request.POST['room_name']
    # username = request.POST['username']
    # if Room.objects.filter(name=room).exists():
    #     return redirect('/'+room+'/?username='+username) #redirecting the user to the existing room and passing the username with it
    # else:
    #     new_room = Room.objects.create(name=room)   #creating the room to redirect the user if room doesnot exist
    #     new_room.save()
    #    return redirect('/'+room+'/?username='+username) 
    return render(request, 'home.html')
    
def send(request):
    # input from ajax 
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(value= message, user= username, room= room_id)
    new_message.save()
    return HttpResponse('Message sent sucessfullly')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values())})

def attendance(request):
    user = request.user
    attendance = Attendance.objects.filter(user=user, check_in__date=now().date()).first()
    if request.method == 'POST':
        if attendance:
            form = CheckOutForm(request.POST)
            if form.is_valid():
                attendance.check_out = form.cleaned_data['check_out']
                attendance.save()
                return redirect('attendance')
        else:
            form = CheckInForm(request.POST)
            if form.is_valid():
                check_in = form.cleaned_data['check_in']
                attendance = Attendance.objects.create(user=user, check_in=check_in)
                return redirect('attendance')
    else:
        if attendance:
            form = CheckOutForm()
        else:
            form = CheckInForm()
    return render(request, 'attendance.html', {'form': form, 'attendance': attendance})
from django.shortcuts import render, redirect

from base.forms import RoomForm
from .models import Room

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Nodejs!'},
#     {'id': 2, 'name': 'UI/UX with Gee Lawrence'},
#     {'id': 3, 'name': 'DevOps to the Moon'}
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('base:home')
            
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('base:home')
            
    
    context = {'form':form}
    return render(request,'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    
    return render(request, 'base/delete.html', {'obj':room})
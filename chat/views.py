from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import ChatRoomForm

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chat/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})


def options(request):
    return render(request, 'chat/choose.html')



@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')  # Redirect to a success page
    else:
        form = ChatRoomForm()

    return render(request, 'chat/createroom.html', {'form': form})
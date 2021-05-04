from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView

from .models import Msg
from .forms import MsgForm, IdForm, PswdForm

def index(request):
    if request.method == 'POST':
        id_usr = request.POST.get('id_usr') 
        return redirect(f'/msg/{id_usr}')
    else:
        usr = IdForm()
        return render(request, 'index.html', {'form': usr})

def create_msg(request):
    form = MsgForm(request.POST)
    id_msg = ''
    if request.method == 'POST':
        if form.is_valid:
            user_msg = request.POST.get('user')
            text_msg = request.POST.get('message')
            paswd_msg = request.POST.get('password')
            user_m = Msg()
            user_m.message = text_msg
            user_m.password = paswd_msg
            user_m.user = user_msg
            user_m.save()
            id_msg = user_m.id
        else:
            form = MsgForm()
    return render(request, 'msg.html', {'form': form, 'id_msg': id_msg})

def msg_detail(request, id):
    messg = get_object_or_404(Msg, id = id)
    user_m = Msg.user
    form = PswdForm(request.POST)
    if request.method == 'POST':
        password_msg = request.POST.get('password')
        password_m = Msg.objects.get(password = password_msg)
        return render(request, 'message.html', {'message': messg, 'user': user_m})
    else:
        form = PswdForm()
    return render(request, 'msg_user.html', {'form': form})
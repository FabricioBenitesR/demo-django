from django.shortcuts import render
from .models import Mensagem

def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})

def sobre(request):
    return render(request, "home/sobre.html")
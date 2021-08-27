from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):#Esta é a view mais simples possível no Django. Para chamar a view, nós temos que mapear a URL - e para isto nós precisamos de uma URLconf.
                   #Para criar uma URLconf no diretório polls, crie um arquivo chamado urls.py. Agora seu diretório da aplicação deve ficar como:
    return HttpResponse("index")

def index3(request):
    return HttpResponse("index3")
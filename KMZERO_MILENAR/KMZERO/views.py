from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'KMZERO/cadastro.html')

def listar(request):
    return render(request, 'KMZERO/listar.html',{'KMZERO':range(50)})

def eventoCadastrar(request):
    return render(request, 'KMZERO/eventoCadastrar.html')

def eventoListar(request):
    return render(request, 'KMZERO/eventoListar.html',{'KMZERO':range(50)})

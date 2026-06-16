from django.urls import path
from .views import home, cadastro, listar, eventoCadastrar, eventoListar

app_name = 'KMZERO'

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('listar/', listar, name='listar'),
    path('eventoCadastrar/', eventoCadastrar, name='eventoCadastrar'),
    path('eventoListar/', eventoListar, name='eventoListar'),
]



# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
    # path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('cadastro/', CadastroView.as_view(), name="cadastro"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo"),
    path('login/', LoginView.as_view(), name="login"),
    path('cadastroUsuario/', cadastroUsuarioView.as_view(), name="cadastroUsuario"),
    path('dash/', dashView.as_view(), name="dash"),
    path('cadastroPessoa/', cadastroPessoaView.as_view(), name="cadastroPessoa"),
    path('form/', formView.as_view(), name="form"),
]

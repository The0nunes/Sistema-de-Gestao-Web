from django.shortcuts import render, redirect, HttpResponse
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required


def livros(request):
    dados = {
        'dados':Livro.objects.all()
    }
    return render(request, 'conteudo/livro.html', context=dados)

def detalhe(request,id_livro):
    dados = {
        'dados': Livro.objects.get(pk=id_livro)
        }
    return render(request, 'conteudo/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        if livro_form.is_valid():
            livro_form.save()
        return redirect('livros')
    else:
        livro_form = LivroForm()
        formulario = {
            'formulario': livro_form
        }
        return render(request, 'conteudo/novo_livro.html', context=formulario)
    

@login_required
def editar(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)
    # novo_investimento -> GET
    if request.method == 'GET':
        formulario = LivroForm(instance=livro)
        return render(request, 'conteudo/novo_livro.html', {'formulario': formulario})
    # caso seja POST
    else:
        formulario = LivroForm(request.POST, instance=livro)
        if formulario.is_valid():
            formulario.save()
        return redirect('livros')

@login_required
def excluir(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)
    if request.method == 'POST':
        livro.delete()
        return redirect('livros')
    return render(request, 'conteudo/confirmar_exclusao.html', {'item':livro})

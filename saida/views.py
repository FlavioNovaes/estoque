from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidasForm

def list_saida(request):
    saida = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {
        'saidas':saida,
    }
    return render(request, template_name, context)

def new_saida(request):
    if request.method == 'POST':
        form = SaidasForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('saida:list_saida')
    else:
        template_name = 'new_saida.html'
        context = {
            'form':SaidasForm(),
        }
        return render(request, template_name, context)

def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    quantidade = saida.quantidade
    print(f'==> {quantidade}')

    if request.method == 'POST':
        form = SaidasForm(request.POST, instance=saida)
        if form.is_valid():
            form.save(commit = False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('saida:list_saida')
    else:
        template_name = 'update_saida.html'
        context = {
            'form': SaidasForm(instance=saida),
            'pk': pk,
        }
        return render(request, template_name, context)

def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    saida.produto.quantidade = saida.produto.quantidade + saida.quantidade
    saida.produto.save()
    saida.delete()
    return redirect('saida:list_saida')
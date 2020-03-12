from django.shortcuts import render, get_object_or_404, reverse, redirect
# from django.http import HttpResponseRedirect, HttpResponse
from .models import Pizza
from .forms import PizzaForm


def list_pizzas(request):
    qs = Pizza.objects.all().order_by('-votes')
    return render(request,
                  'list.html',
                  {'qs_pizzas':qs}
                  )


def detail(request, id):
    qs = get_object_or_404(Pizza, id=id)
    return render(request,
                  'detail.html',
                  {'pizza': qs}
                  )


def add(request):
    pForm = PizzaForm(request.POST or None)
    if pForm.is_valid():
        pForm.save()
        return redirect(reverse('pizzas:list'))
    return render(request,
                  'create.html',
                  {'pForm': pForm}
                  )


def delete(request, id):
    qs = get_object_or_404(Pizza, id=id)
    if request.method == 'POST':
        qs.delete()
        return redirect(reverse('pizzas:list'))

    return render(request,
                  'delete.html',
                  {'qs': qs}
                  )


def edit(request, id):
    qs = get_object_or_404(Pizza, id=id)
    pForm = PizzaForm(request.POST or None, instance=qs)
    if pForm.is_valid():
        pForm.save()
        return redirect(reverse('pizzas:list'))
    else:
        print(pForm.errors)
    
    return render(request,
                  'edit.html',
                  {'pizza': qs,
                   'pForm': pForm}
                  )


def vote(request, id):
    qs = get_object_or_404(Pizza, id=id)
    if request.method == 'POST':
        qs.votes = int(qs.votes)+1
        qs.save()
        return redirect(reverse('pizzas:list'))

    return render(request,
                  'vote.html',
                  {'qs': qs}
                  )



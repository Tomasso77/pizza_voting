from django.shortcuts import render, get_object_or_404, reverse, redirect
# from django.http import HttpResponseRedirect, HttpResponse
from .models import Pizza, Topping, ToppingAmount
from .forms import PizzaForm, ToppingForm, ToppingAmountForm

def list_pizzas(request):
    qs_pizzas = Pizza.objects.all().order_by('-votes')
    top_amt = ToppingAmount.objects.all()
    
    return render(request,
                  'list.html',
                  {'qs_pizzas':qs_pizzas,
                   'top_amt': top_amt}
                  )


def detail(request, id):
    qs = get_object_or_404(Pizza, id=id)
    top_amt = ToppingAmount.objects.filter(pizza_id = qs.id)

    return render(request,
                  'detail.html',
                  {'pizza': qs,
                   'top_amt': top_amt }
                  )


def add(request):
    pForm = PizzaForm(request.POST or None)
    if pForm.is_valid():
        pizza = pForm.save()
        return redirect(reverse('pizzas:add_toppings', kwargs={"id":pizza.id}))
    
    return render(request,
                  'create.html',
                  {
                      'pForm': pForm,
                   }
                  )

def add_toppings(request, id):
    taForm = ToppingAmountForm(request.POST or None)
    pizza = get_object_or_404(Pizza, id=id)
    toppings = ToppingAmount.objects.filter(pizza=pizza.id)

    if taForm.is_valid():
        cd = taForm.cleaned_data
        try:
            ta_query = ToppingAmount.objects.get(pizza=cd['pizza'], topping=cd['topping'])
            ta_query.amount = cd['amount']
            ta_query.save()
        except ToppingAmount.DoesNotExist:
            taForm.save()
    return render(request,
                  'add_toppings.html',
                  {'taForm': taForm,
                   'pizza': pizza,
                   'toppings': toppings}
                  )

def add_new_topping(request):
    tForm = ToppingForm(request.POST or None)
    if tForm.is_valid():
        cd = tForm.cleaned_data
        if not Topping.objects.filter(topping=cd['topping']):
            tForm.save()
    
    return render(request,
                  'add_new_topping.html',
                  {
                      'tForm': tForm,
                  })
    # pizza = get_object_or_404(Pizza, id=id)
    # toppings = ToppingAmount.objects.filter(pizza=pizza.id)

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
        # cd = pForm.cleaned_data
        # ta_query = ToppingAmount.objects.filter(pizza=cd.pizza, topping=cd.topping)
        # ta_query.remove()
        # # if ta_query.exist():
        # #     ta_query.amount = cd.amount
        # #     ta_query.save()
        # # else:
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



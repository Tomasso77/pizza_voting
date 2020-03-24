from django import forms
from .models import Pizza, Topping, ToppingAmount


class PizzaForm(forms.ModelForm):
    
    # topping_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    # amount = forms.IntegerField(required=False, initial=0)
    
    class Meta:
        model = Pizza
        toppings = forms.ModelChoiceField(queryset=Topping.objects.all())
        fields = ['name']
    
    def save(self, commit=True):
        pizza = super(PizzaForm, self).save()
    #     topping_id = self.cleaned_data.get('topping_id')
    #     topping = Topping.objects.get(id=topping_id)
    #     amount = self.cleaned_data.get('amount')
    #     ToppingAmount.objects.create(pizza=pizza, topping=topping, amount=amount)
    # #
        return pizza


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping']


class ToppingAmountForm(forms.ModelForm):
    class Meta:
        model = ToppingAmount
        fields = ['pizza', 'topping', 'amount']
    #
    # def save(self):
    #     topping1 = self.cleaned_data.get('topping')
    #     print(topping1)
    #     pizza1 = self.cleaned_data.get('pizza')
    #     print(pizza1)
    #     qs = ToppingAmount.objects.filter(pizza=pizza1).filter(topping=topping1)
    #     print(qs)
    #     if (qs):
    #         am = super(ToppingAmountForm, self).update()
    #         return am
    #     else:
    #         am = super(ToppingAmountForm, self).save()
    #         return am

            

        #     topping = Topping.objects.get(id=topping_id)
        #     amount = self.cleaned_data.get('amount')
        #     ToppingAmount.objects.create(pizza=pizza, topping=topping, amount=amount)
    
        

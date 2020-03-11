from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name',
                  'topping1', 'topping1_amount',
                  'topping2', 'topping2_amount',
                  'topping3', 'topping3_amount',
                  'topping4', 'topping4_amount',
                  'topping5', 'topping5_amount',
                  'topping6', 'topping6_amount',
                  'topping7', 'topping7_amount',
                  'topping8', 'topping8_amount',
                  'topping9', 'topping9_amount',
                  'topping10', 'topping10_amount',
                  'votes'
                  ]

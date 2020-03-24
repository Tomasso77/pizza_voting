from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from pizzas.models import Pizza


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'name', 'slug',
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
                  'nr_of_toppings', 'total_toppings_amount',
                  'votes'
                  ]
        read_only_fields = ['id']
#
class PizzaMiniSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = [ 'id', 'name', 'slug', 'votes' ]
        read_only_fields = ['id']
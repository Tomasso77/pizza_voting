from django.test import TestCase
from pizzas.models import Pizza
from django.utils.text import slugify



class PizzaTestCase(TestCase):
    def setUp(self):
        Pizza.objects.create(name="Classic pizza with mushrooms",
                             topping1="Mozzarella Cheese", topping1_amount="50",
                             topping2="Tomato sauce", topping2_amount="10",
                             topping3="Pepperoni", topping3_amount="15",
                             topping4="Mushrooms", topping4_amount="20",
                             )
    
    def test_nr_toppings(self):
        """Test that nr of toppings is correctly calculated"""
        classic_pizza = Pizza.objects.get(name="Classic pizza with mushrooms")
        self.assertEqual(classic_pizza.nr_of_toppings, 4)
        
    def test_total_toppings_amout(self):
        """Test that total toppings amount is correctly calculated"""
        classic_pizza = Pizza.objects.get(name="Classic pizza with mushrooms")
        self.assertEqual(classic_pizza.total_toppings_amount, 95)
        
    def test_slug(self):
        """Test that slug is correctly clreated"""
        classic_pizza = Pizza.objects.get(name="Classic pizza with mushrooms")
        pizza_slug = slugify("Classic pizza with mushrooms")  # 'classic-pizza-with-mushrooms'
        self.assertEqual(classic_pizza.slug, pizza_slug)
        
    def test_vote(self):
        classic_pizza = Pizza.objects.get(name="Classic pizza with mushrooms")
        self.assertEqual(classic_pizza.votes, 0)

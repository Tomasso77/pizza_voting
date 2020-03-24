from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Topping(models.Model):
    topping = models.CharField(max_length=100)

    def __str__(self):
        return self.topping
    

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,
                            unique=True,
                            blank=True)
    
    toppings = models.ManyToManyField(Topping, through='ToppingAmount', related_name='pizzas')
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        super(Pizza, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pizzas:detail',
                       args=[self.id])

    def get_edit_url(self):
        return f"{self.get_absolute_url()}edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}delete"
    
    def get_vote_url(self):
        return f"{self.get_absolute_url()}vote"
    #
    @property
    def total_toppings_amount(self):
        tot_top_amnt = 0
    #     for i in range(1, 11):
    #         tot_top_amnt += int(eval('self.topping'+str(i)+'_amount'))
    #     return tot_top_amnt
    #
    @property
    def nr_of_toppings(self):
        nr_of_top = 0
    #     for i in range(1, 11):
    #         if eval('self.topping'+str(i)) != '':
    #             nr_of_top += 1
    #     return nr_of_top


class ToppingAmount(models.Model):
    REGULAR = 1
    DOUBLE = 2
    TRIPLE = 3
    AMOUNT_CHOICES = (
        (REGULAR, 'Regular'),
        (DOUBLE, 'Double'),
        (TRIPLE, 'Triple'),
    )
    
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)
    
    def __str__(self):
        return self.pizza.name + ' with ' + self.get_amount_display() + ' ' + self.topping.topping
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,
                            unique=True,
                            blank=True)
    topping1 = models.CharField(max_length=100, default="", blank=True)
    topping2 = models.CharField(max_length=100, default="", blank=True)
    topping3 = models.CharField(max_length=100, default="", blank=True)
    topping4 = models.CharField(max_length=100, default="", blank=True)
    topping5 = models.CharField(max_length=100, default="", blank=True)
    topping6 = models.CharField(max_length=100, default="", blank=True)
    topping7 = models.CharField(max_length=100, default="", blank=True)
    topping8 = models.CharField(max_length=100, default="", blank=True)
    topping9 = models.CharField(max_length=100, default="", blank=True)
    topping10 = models.CharField(max_length=100, default="", blank=True)
    topping1_amount = models.IntegerField(default=0)
    topping2_amount = models.IntegerField(default=0)
    topping3_amount = models.IntegerField(default=0)
    topping4_amount = models.IntegerField(default=0)
    topping5_amount = models.IntegerField(default=0)
    topping6_amount = models.IntegerField(default=0)
    topping7_amount = models.IntegerField(default=0)
    topping8_amount = models.IntegerField(default=0)
    topping9_amount = models.IntegerField(default=0)
    topping10_amount = models.IntegerField(default=0)
    nr_of_toppings = models.IntegerField(default=0)
    total_toppings_amount = models.IntegerField(default=0)
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        self.nr_of_toppings = 0
        self.total_toppings_amount = 0
        
        for i in range(1, 11):
            self.total_toppings_amount += int(eval('self.topping'+str(i)+'_amount'))
            if eval('self.topping'+str(i)) != '':
                self.nr_of_toppings += 1
            
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

from django.test import TestCase, Client
from django.urls import reverse
from pizzas.models import Pizza
from django.utils.text import slugify

import json


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.pizza1 = Pizza.objects.create(name='pizza1')
        self.list_url = reverse('pizzas:list')
        self.detail_url = reverse('pizzas:detail', args=[self.pizza1.id])
        self.add_url = reverse('pizzas:add')
        self.edit_url = reverse('pizzas:edit', args=[self.pizza1.id])
        self.delete_url = reverse('pizzas:delete', args=[self.pizza1.id])
        self.vote_url = reverse('pizzas:vote', args=[self.pizza1.id])

    def test_list_pizzas_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
    
    def test_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')
        
    def test_add_GET(self):
        response = self.client.get(self.add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
        
    def test_edit_GET(self):
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')
        
    def test_delete_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')
        
    def test_delete_POST(self):
       self.pizza_temp = Pizza.objects.create(
            name='New Tested Pizza',
            topping1='cheese', topping1_amount= '50',
        )
       response = self.client.post(reverse('pizzas:delete', args=[self.pizza_temp.id]))
       self.assertEquals(response.status_code, 302)
        
    def test_vote_GET(self):
        """Test vote view (GET method)"""
        response = self.client.get(self.vote_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote.html')
    
    def test_vote_POST(self):
        """Test voting - POST method"""
        response = self.client.post(self.vote_url)          # voting
        self.pizza2 = Pizza.objects.get(name='pizza1')      # query after voting
        self.assertEquals(response.status_code, 302)        # redirection [HTTP status = 302] after voting
        self.assertEquals(self.pizza2.votes, 1)             # 1 vote

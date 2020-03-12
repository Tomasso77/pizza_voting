from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pizzas.views import list_pizzas, add, delete, detail, edit, vote


class TestUrls(SimpleTestCase):
    """Test of urls"""
    def test_list_url_resolves(self):
        url = reverse('pizzas:list')
        self.assertEquals(resolve(url).func, list_pizzas)
    
    def test_add_url_resolves(self):
        url = reverse('pizzas:add')
        self.assertEquals(resolve(url).func, add)
    
    def test_detail_url_resolves(self):
        url = reverse('pizzas:detail', args=[5])
        self.assertEquals(resolve(url).func, detail)
    
    def test_edit_url_resolves(self):
        url = reverse('pizzas:edit', args=[7])
        self.assertEquals(resolve(url).func, edit)
        
    def test_delete_url_resolves(self):
        url = reverse('pizzas:delete', args=[12])
        self.assertEquals(resolve(url).func, delete)
        
    def test_vote_url_resolves(self):
        url = reverse('pizzas:vote', args=[12])
        self.assertEquals(resolve(url).func, vote)
        
    
from django.urls import path, include
from . import views

app_name = "pizzas"

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/vote/', views.vote, name='vote'),
    path('api/', include('pizzas.api.urls')),
    
]

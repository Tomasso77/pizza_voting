from django.urls import path, include
from .views import PizzaListAPIView, PizzaRUDView, PizzaVoteView


urlpatterns = [
    path('', PizzaListAPIView.as_view(), name='list-api'),
    path('<int:id>/', PizzaRUDView.as_view(), name='rud-api'),
    path('<int:id>/vote/', PizzaVoteView.as_view(), name='vote-api'),
]

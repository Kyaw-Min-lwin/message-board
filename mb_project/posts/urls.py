from django.urls import path
from .views import HomePageView, second_home

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('secondHome', second_home, name='secondHome')
]
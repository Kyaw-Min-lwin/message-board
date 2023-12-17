from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'

def second_home(request):
    posts = Post.objects.all()
    return render(request, 'second_home.html', {'posts' : posts})
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post

"""
posts = [
    {
        'owner': 'Gourab Saha',
        'location': 'Sylhet',
        'content': 'Hostel',
        'date_posted': '1 December,2020'
    },
    {
        'owner': 'Sourav Saha',
        'location': 'Gopalganj',
        'content': 'Family House',
        'date_posted': '31 December,2020'
    },
    {
        'owner': 'Md. Habib',
        'location': 'BBaria',
        'content': 'Ladies Hostel',
        'date_posted': '1 December,2021'
    }
]

"""
def home(request):
    context ={
#        'posts': posts
         'posts': Post.objects.all()

    }
    return render (request ,'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post



def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

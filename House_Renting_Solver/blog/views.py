from django.shortcuts import render
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


def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

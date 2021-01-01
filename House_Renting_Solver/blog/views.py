from django.shortcuts import render
from django.http import HttpResponse

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
    }
]

def home(request):
    context ={
        'posts': posts
    }
    return render (request ,'blog/home.html', context)


def about(request):
    return render (request, 'blog/about.html')

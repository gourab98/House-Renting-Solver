from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)
from django.http import HttpResponse
from .models import Post,Post1,Post3
from .forms import CreatePostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from users.models import Register
    

def home(request):
    return render(request,'blog/home.html',{})


def PostList(request):
    if 'q' in request.GET:
        q = request.GET['q']
        context = {
            'post3s' : Post3.objects.filter(address__icontains=q).order_by('-date_posted')
        }
    else:
        context = {
        'post3s' : Post3.objects.all().order_by('-date_posted')
    }

    return render(request, 'blog/home1.html', context)

class UserPostListView(ListView):
    model = Post3
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'post3s'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post3.objects.filter(owner=user).order_by('-date_posted')

class UserProfileView(ListView):
    model = Register
    template_name = 'blog/user_profile.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'register'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Register.objects.filter(user=user)


class PostDetailView(DetailView):
    model = Post3

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    model = Post1

   
    
    def form_valid(self, form):
        post1 = form.save(commit=False)
        form.instance.owner = self.request.user
        objects = form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post3
    fields = ['house_type','renter_preference','family_member','religion_preference','occupation_priority',
            'address','floor','bed_room','bed_room_image','drawing_room','drawing_room_image','dinning_room','dinning_room_image','kitchen',
            'kitchen_room_image','bathroom','bath_room_image','washing_Machine','hot_water','IPS','Generator','Belcony','Oven','lift','refrigerator','sofa','wifi','ac','television','gas','security',
            'parking','house_rent','electricity_rent','gas_rent','water_rent','service_rent','rent_date','any_special_instructions']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post3
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False



def about(request):
    if 'q' in request.GET:
        q = request.GET['q']
        context = {
            'post3s' : Post3.objects.filter(address__icontains=q)
        }
    else:
        context = {
        'post3s' : Post3.objects.all()
    }

    return render(request, 'blog/home.html', context)

@login_required
def PostCreate(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            post1 = form.save(commit=False)
            post1.owner = request.user
            post1.save()
            img_obj = form.instance
            messages.success(request, f'Your post has been created')
            return redirect('blog-home') 
    else:
        form = CreatePostForm()
    return render(request,'blog/index.html',{'form':form})     



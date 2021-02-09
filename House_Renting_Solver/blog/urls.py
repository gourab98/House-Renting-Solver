from django.urls import path
from .views import PostDetailView, PostUpdateView, PostDeleteView, UserPostListView,UserProfileView
from . import views

urlpatterns = [
     
     path('', views.home, name='template-home'),
     path('home/', views.PostList, name='blog-home'),
     path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
     path('post/<str:username>', UserProfileView.as_view(), name='user-profile'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     #path('post/new/', PostCreateView.as_view(), name='post-create'),
     path('post/new/', views.PostCreate, name='post-create'),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
#    path('', views.home, name='blog-home'),
     path('about/', views.about, name='blog-about'),
]

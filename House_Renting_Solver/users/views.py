from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,UserRegistrationForm,UserRegistrationUpdateForm
from .models import Register
from django.core import serializers

def register(request):
    if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            form1 = UserRegistrationForm(request.POST)
            if  form.is_valid() and form1.is_valid():
                user = form.save()
                user.save()
                register = form1.save(commit=False)
                register.user = user
                register.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in!')
                return redirect('login')
    else:
         form = UserRegisterForm(request.POST)
         form1 = UserRegistrationForm(request.POST)
    return render(request, 'users/register.html', {'form': form,'form1':form1})

@login_required
def profile(request):
    user = request.user
    context = {
        'register': Register.objects.all()
    }
    template = 'users/profile.html'
    return render(request,template,context)



@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        v_form = UserRegistrationUpdateForm(request.POST,request.FILES,instance=request.user.register)
        p_form = ProfileUpdateForm(request.POST,
        request.FILES,
        instance = request.user.profile)

        if u_form.is_valid() or v_form.is_valid() or p_form.is_valid():
            u_form.save()
            v_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        v_form = UserRegistrationUpdateForm(instance=request.user.register)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form':u_form,
        'v_form':v_form,
        'p_form':p_form
    }
    return render(request,'users/update.html',context)



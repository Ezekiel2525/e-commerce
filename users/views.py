from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            
            return redirect('login')
    else:
        form = UserRegistrationForm()
        
        
    context = {'form' : form}
    
    return render(request, 'users/signup.html', context)



@login_required
def profile(request):
    return render(request, 'users/profile.html')


def update(request):
    if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                profile, created = Profile.objects.get_or_create(user=request.user)
                p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
                
                p_form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('profile')
            context = {'u_form' : u_form, 'p_form' : p_form}
            
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        p_form = ProfileUpdateForm(instance=profile)
        
    context = {'u_form' : u_form, 'p_form' : p_form} 
    return render(request, 'users/updateprofile.html' , context)
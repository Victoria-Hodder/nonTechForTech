from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # now inherits from forms.py

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #saves the users data - hashes password automatically
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You may now login') #import messages
            return redirect('login') #name of url path
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required # this needs to be added otherwise anyone can edit the profile
def profile(request):

    # if statement checks the forms are valid and saves the info
    if request.method == 'POST':
        # these requests are added so your current info is already in the form
        u_form = UserUpdateForm(request.POST, instance=request.user) 
        p_form = ProfileUpdateForm(request.POST, # for POST data
                                    request.FILES, #for profile pics (images)
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): #if both valid, then you can save it
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile') # post-get-redirect pattern; stops you running another post request

    else:
        u_form = UserUpdateForm(instance=request.user) 
        # shows current info even if it's not to a logged user
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = { # context is a dictionary of what the form needs
        'u_form' : u_form,
        'p_form' : p_form
    }

    # once you have a context you can create a form in the profile.html

    return render(request, 'users/profile.html', context)


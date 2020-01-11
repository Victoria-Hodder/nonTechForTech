from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(): # keep configurations in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#video 9 below - this is a model form - allows us to work with a specific database model

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email']


# import Profile (see above)

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['bio', 'image']

# these are created together to make one form in the template
#import into views.py
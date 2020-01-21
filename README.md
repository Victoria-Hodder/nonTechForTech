# Non Tech for Tech


> Non Tech for Tech is a blog where developers from alternative backgrounds can explain how their non-coding skills help their daily code.

## Setup ##

I assume Python 3.x or higher is installed. 

## Tech used ##

Built in:

    Python 3.x
    Django 2.2.5

## Features ##

Users can register to create an account with the possibility thereafter to log in and out.

They can edit their profiles (including changing their profile picture)

Registered users may also edit and delete their own blog posts.


## Getting it to run ##

Before you start, please create a virual environment in the project folder and activate it (example iOS):

    # create virutal environment (if `env` is the name you want 
    # to give to your virtual environment:
    
    $ python3 -m venv env
    
    # activate virutal env
    $ source env/bin/activate

In order to install all nececsary libraries please:
	
	pip install -r requirements.txt  

Now run the app by using following command:

	$ python manage.py runserver
	
The app should now run on your local server. To test the different endpoints, please go to **http://127.0.0.1:8000/**


## Testing ##

This app is not yet tested.

## Documentation ##

For the Django Documentation: **https://docs.djangoproject.com/en/2.2/**
For Python Documentation: **https://docs.python.org/3/**

## Limitations ##

This app is not yet tested
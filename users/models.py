from django.db import models
from django.contrib.auth.models import User
from PIL import Image #pillow for images

#Video 8 and 9 for Corey, also this video:
# https://www.youtube.com/watch?v=kdzevMFg3NM 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=250, blank=True)

    def __str__(self): #how we want it to be displayed
        return f'{self.user.username} Profile'

    # migrate! Register models in admin


    # below is for resizing images

    def save(self):
        super().save() #run save method of our parent class - grabs image from above

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



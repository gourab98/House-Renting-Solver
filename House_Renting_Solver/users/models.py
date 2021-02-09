from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

#    def save(self):
#        super().save()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


GENDER_CHOICES = (
    ('one','Man'),
    ('two','Woman'),
    ('three','Others'),
)
MARITAL_CHOICES = (
    ('one','Unmarried'),
    ('two','Married'),
)

class Register(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    occupation = models.CharField(max_length = 150)
    address = models.CharField(max_length = 150)
    gender = models.CharField(max_length=5,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=12, null=True)
    religion = models.CharField(max_length = 20,null=True)
    marital_status = models.CharField(max_length=3,choices=MARITAL_CHOICES)
    nid = models.CharField(max_length=11)

    def __str__(self):
        return self.user.username



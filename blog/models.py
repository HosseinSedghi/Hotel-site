from django.db import models

# Create your models here.


class SliderHome(models):
    image = models.ImageField(upload_to='images/slider_images')



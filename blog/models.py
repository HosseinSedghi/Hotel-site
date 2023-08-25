from django.db import models

# Create your models here.


class SliderHome(models.Model):
    image = models.ImageField(upload_to='images/slider_images')


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=20)
    about_site = models.TextField(null=True, blank=True)
    email = models.EmailField()
    fax = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    copy_right_text = models.CharField(max_length=50)

    def __str__(self):
        return self.site_name

class LinkBox(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Links(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=130)
    box = models.ForeignKey(LinkBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
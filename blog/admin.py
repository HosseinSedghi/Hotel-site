from django.contrib import admin

from blog.models import LinkBox, Links, SiteSettings, SliderHome

# Register your models here.


admin.site.register(SliderHome)
admin.site.register(SiteSettings)
admin.site.register(LinkBox)
admin.site.register(Links)
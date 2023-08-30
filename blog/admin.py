from django.contrib import admin

from blog.models import LinkBox, Links, SiteSettings, SliderHome, Ticket, Room, Gallery, GalleryCategory, Blog

# Register your models here.

admin.site.register(SliderHome)
admin.site.register(SiteSettings)
admin.site.register(LinkBox)
admin.site.register(Links)
admin.site.register(Ticket)
admin.site.register(Room)
admin.site.register(GalleryCategory)
admin.site.register(Gallery)
admin.site.register(Blog)
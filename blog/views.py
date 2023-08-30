from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from blog.forms import TicketForm
from blog.models import SliderHome, SiteSettings, LinkBox, Ticket, Room, Gallery, GalleryCategory, Blog
from packages.converters import convert_list_to_index


# Create your views here.


class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        sliders = list(SliderHome.objects.all())
        context['sliders'] = sliders[:-1]
        context['sliders_count'] = convert_list_to_index(sliders[:-1])
        context['about_image'] = sliders[-1:]
        context['site'] = SiteSettings.objects.all().first()
        context['rooms'] = Room.objects.all()[:6]
        context['galleries'] = Gallery.objects.all()[:8] # todo: get random gallery
        context['blogs'] = Blog.objects.filter(is_publish=True)[:3]
        return context


class TicketView(View):
    def get(self, request):
        form = TicketForm()
        if request.user.is_authenticated:
            return render(request, 'blog/contact-us.html', {
                'form': form
            })
        else:
            return render(request, 'blog/contact-us.html', {})

    def post(self, request):
        if request.user.is_authenticated:
            form = TicketForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                text = form.cleaned_data.get('text')
                user = request.user

                new_ticket = Ticket(title=title, text=text, user_id=user.id)
                new_ticket.save()

        return redirect('ticket-page')


class RoomListView(TemplateView):
    template_name = 'blog/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rooms'] = Room.objects.all()
        return context


class GalleryView(TemplateView):
    template_name = 'blog/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        categories = GalleryCategory.objects.all()
        gallery_list = []
        for category in categories:
            item = {
                'id': category.id,
                'name': category.name,
                'gallery': category.gallery_set.all()[:4],
                'all_gallery': category.gallery_set.all()
            }
            gallery_list.append(item)
        context['gallery_list'] = gallery_list
        return context


class BlogView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['articles'] = Blog.objects.filter(is_publish=True)
        return context
# ========================================= Partial classes ========================================= #

class HeaderPartial(TemplateView):
    template_name = 'includes/header-partial.html'


class FooterPartial(TemplateView):
    template_name = 'includes/footer-partial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['boxes'] = LinkBox.objects.all()
        context['site'] = SiteSettings.objects.all().first()
        return context

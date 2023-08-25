from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import SliderHome, SiteSettings, LinkBox
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
        return context


# Partial classes

class HeaderPartial(TemplateView):
    template_name = 'includes/header-partial.html'


class FooterPartial(TemplateView):
    template_name = 'includes/footer-partial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['boxes'] = LinkBox.objects.all()
        context['site'] = SiteSettings.objects.all().first()
        return context
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
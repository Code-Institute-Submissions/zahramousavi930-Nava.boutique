from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class Home_page(TemplateView):
    template_name = 'home_page.html'
    def get_context_data(self, **kwargs):

        context=super(Home_page, self).get_context_data()


        return context

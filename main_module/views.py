from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
# Create your views here.



class Home_page(TemplateView):
    template_name = 'home_page.html'


    def get_context_data(self, **kwargs):

        context=super(Home_page, self).get_context_data()
        context['products']=models.Products.objects.all()[:6]
        context['category']=models.Category.objects.all()
        print(self.request.user.id)
        return context



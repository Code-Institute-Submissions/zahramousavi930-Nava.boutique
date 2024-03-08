from django.shortcuts import redirect ,render,reverse
from django.views.generic import TemplateView,DetailView
from django.views import View
from django.http import JsonResponse
from . import models
from . import forms
import json
import random
from order_module.models import OrderDetail





class Home_page(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super(Home_page, self).get_context_data(**kwargs)
        context['products_discount'] = models.Products.objects.exclude(discount=0)
        context['products'] = models.Products.objects.filter(discount=0)[:6]
        context['category'] = models.Category.objects.all()
        return context






def add_variable_to_context(request):
    if request.user.is_authenticated:
        data = OrderDetail.objects.filter(order__userr_id=request.user.id, final_price=None).count()
    else:
        data = 0
    return {
        'data': data
    }



def newsteller(request):

    if request.POST:
        email =request.POST.get('newstelleremail')
        try:
            new_email=models.News_teller(
                email=email
            )
            new_email.save()


            return redirect('home_pgae')

        except:
            return redirect('home_pgae')

    else:
        return redirect('home_pgae')





def remove_news_teller(request):


    email = request.POST.get('removenewstelleremail')
    models.News_teller.objects.filter(email__exact=email).delete()

    return redirect('home_pgae')






class Products(DetailView):
    template_name = 'products.html'
    model = models.Products
    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data()
        context['selected_product']=models.Products.objects.filter(slug__exact=self.kwargs['slug']).first()
        context['comment_form']=forms.comments
        context['comments']=models.add_comments.objects.filter(product_id=self.kwargs['pk'])
        return context
    
    def get_absolute_url(self):
        return reverse('products_pgae', args=[self.pk])



def add_comments_part(request):
    data = json.loads(request.body.decode("utf-8"))
    id = data['id']
    text = data['text']
    email = data['email']
    rate= data['rate']

    if rate ==0:
        rate =1



    if request.user.is_authenticated:
        new_comments=models.add_comments(
            email=email,
            text=text,
            user_id=request.user.id,
            product_id=id,

        )
        old =models.Products.objects.filter(id=id).first()
        old_value=old.rate
        old_value +=int(rate)

        models.Products.objects.update(rate=old_value)
        new_comments.save()
        return JsonResponse({
            'status': 'ok',
            'message': 'refresh page to see your comment.'
        })
    else:
        return JsonResponse({
            'status': 'no',
            'message':'first login!'
        })












class all_peoducts(View):
    def get(self,reqiest):
        all_products=models.Products.objects.all()

        context={
            'all_product':all_products
        }
        return render(reqiest,'all products.html',context)

    def post(self,request):
        value =request.POST.get('select')

        if value == '2':
            low_prod=models.Products.objects.order_by('price')

            context={
                'low':low_prod
            }
            return render(request, 'all products.html', context)


        if value == '3':
            high_prod = models.Products.objects.order_by('-price')

            context={
                'high':high_prod
            }
            return render(request, 'all products.html', context)

        if value == '4':
            a_to_z_prod = models.Products.objects.order_by('name')

            context = {
                'high': a_to_z_prod
            }
            return render(request, 'all products.html', context)

        if value == '5':
            z_to_a_prod = models.Products.objects.order_by('-name')

            context = {
                'high': z_to_a_prod
            }
            return render(request, 'all products.html', context)



        else:
            return redirect('all_products_pgae')
















class category(TemplateView):
    template_name = 'category_products.html'


    def get_context_data(self, **kwargs):
        context = super(category, self).get_context_data()
        context['cat_prod']=models.Products.objects.filter(category=self.kwargs['id'])
        context['cat_name']=models.Products.objects.filter(category=self.kwargs['id']).first()


        return context



class contact_with_us(TemplateView):
    template_name = 'contac_with_us.html'


    def get_context_data(self, **kwargs):
        context=super(contact_with_us, self).get_context_data()
        context['footer']=models.contact_with_us.objects.all()
        context['contact_form']=forms.contact_form
        return context






def save_contact_us(request):

    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        text=request.POST.get('text')

        try:
            new_contact=models.contact(
                name=name,
                email=email,
                text=text
            )
            new_contact.save()
            return redirect('home_pgae')

        except:
            return redirect('home_pgae')

    return redirect('home_pgae')






def search(request):

    name=request.POST.get('search')

    result=models.Products.objects.filter(name__icontains=name).all()

    context={
        'result':result
    }
    return render(request,'search.html',context)

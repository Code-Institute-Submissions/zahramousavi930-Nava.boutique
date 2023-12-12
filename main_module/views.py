from django.shortcuts import redirect
from django.views.generic import DetailView,TemplateView
from . import models
from . import forms
# Create your views here.



class Home_page(TemplateView):
    template_name = 'home_page.html'


    def get_context_data(self, **kwargs):

        context=super(Home_page, self).get_context_data()
        context['products']=models.Products.objects.all()[:6]
        context['category']=models.Category.objects.all()
        print(self.request.user.id)
        return context



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




class Products(DetailView):
    template_name = 'products.html'
    model = models.Products
    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data()
        context['selected_product']=models.Products.objects.filter(slug__exact=self.kwargs['slug']).first()
        context['comment_form']=forms.comments
        context['comments']=models.add_comments.objects.filter(product_id=self.kwargs['pk'])
        return context





def add_comments_part(request):
    data = json.loads(request.body.decode("utf-8"))
    id = data['id']
    text = data['text']
    email = data['email']



    if request.user.is_authenticated:
        new_comments=models.add_comments(
            email=email,
            text=text,
            user_id=request.user.id,
            product_id=id
        )
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

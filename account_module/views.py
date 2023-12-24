from django.http import Http404 ,HttpResponseRedirect,JsonResponse,HttpResponse
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic.edit import UpdateView
from django.views import View
from . import forms
from . import models
from django.utils.crypto import get_random_string
from .utils.email_service import send_email
from django.contrib.auth import login, logout
from main_module.models import Products
from main_module import models
from main_module.forms import order_detail_form
import json
from NovaBoutique import settings
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from account_module.models import User
import random


class Profile(View):

    def get(self,request):
        final_order =models.OrderDetail.objects.filter(order__is_paid=True, order__userr=self.request.user)

        fav=models.Products.objects.filter(favorit=self.request.user.id)
        user=models.User.objects.filter(id=self.request.user.id).first()
        delivary_data=models.order_data.objects.filter()

        context={
            'order':final_order,
            'fav':fav,
            'user':user,

            'delivary_data':delivary_data
        }



        return render(request,'profile.html',context)




def detailcart(request,pk):

    detail=models.order_data.objects.filter(which_order=pk).get()
    payment_datea=models.OrderDetail.objects.filter(pk=pk).get()

    return render(request,'detailcart.html',{'detail':detail,'payment_datea':payment_datea})


@csrf_exempt
def stripe_webhook(request):
        payload = request.body
        sig_header =request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except ValueError as e:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            return HttpResponse(status=400)

        if event['type'] == 'checkout.session.completed':
            amount = event['data']['object']
            user_id = amount['metadata']['user_id']
            total=amount['amount_total']

            full_name = amount['metadata']['full_name']
            email_address = amount['metadata']['email_address']
            phone_number = amount['metadata']['phone_number']
            street_address1 = amount['metadata']['street_address1']
            town_or_city = amount['metadata']['town_or_city']
            country_state_or_location = amount['metadata']['country_state_or_location']
            post_code = amount['metadata']['post_code']
            country = amount['metadata']['country']







            order_basket=models.Order.objects.filter(is_paid=False,userr_id=user_id).all()

            for order in order_basket:
                if order.is_paid == False:
                     order.is_paid = True
                     order.payment_date =timezone.now()


                     order.save()

                if order.payment_date == None:
                    order.delete()
                    order.save()




            order_detail_final_price=models.OrderDetail.objects.filter(final_price=None,order__userr=user_id).all()
            total_price='{}'.format(total)[:-2]
            for orders in order_detail_final_price:
                if orders.final_price == None:
                    orders.final_price = total_price
                    orders.save()





            user=models.User.objects.filter(id=user_id).first()





            new_data=models.order_data(
                full_name=full_name,
                email_address=email_address,
                phone_number=phone_number,
                street_address1=street_address1,
                town_or_city=town_or_city,
                country_state_or_location=country_state_or_location,
                post_code=post_code,
                country=country,
                which_user=user

            )
            new_data.save()
            for orderss in order_detail_final_price:
                new_data.which_order.add(orderss)



            main_email=email_address


            send_email('new order', main_email, {'order_basket': order_detail_final_price,'date':new_data,}, 'email_part/order.html')


        return HttpResponse(status=200)




class Edit_profilr(UpdateView):
        template_name = 'edit_user_detail.html'
        model =  User
        fields = ['first_name','last_name','email','username','phone_number']

        success_url = 'profile'


        def get_success_url(self):
            return reverse('profile')


class Shoping_cart(View):
    def get(self,request):
         current_order, created = models.Order.objects.get_or_create(is_paid=False, userr_id=self.request.user.id)

         total_amount = 0
         for order_detail in current_order.orderdetail_set.all():
              total_amount += order_detail.product.price * order_detail.count



         context={
             'order_form':order_detail_form(),
             'order':current_order,
             'sum':total_amount
         }

         return render(request ,'shoping_cart.html',context)

    def post(self,request):
        if request.POST:
            current_order, created = models.Order.objects.get_or_create(is_paid=False, userr_id=self.request.user.id)
            order_detail_id = models.OrderDetail.objects.filter(final_price=None, order__userr=self.request.user.id)


            total_amount = 0
            products_name =[]
            for order_detail in current_order.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
                products_name.append(order_detail.product.name)

            full_name = request.POST.get('full_name')
            email_address = request.POST.get('email_address')
            phone_number = request.POST.get('phone_number')
            street_address1 = request.POST.get('street_address1')
            town_or_city = request.POST.get('town_or_city')
            country_state_or_location = request.POST.get('country_state_or_location')
            post_code = request.POST.get('post_code')
            country = request.POST.get('country')

            stripe.api_key = settings.STRIPE_SECRET_KEY
            host = self.request.get_host()
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': '{}'.format(total_amount * 100),
                            'product_data': {
                             'name':'Nova'

                            },
                        },
                        'quantity': 1,
                    },
                ],
                metadata={
                    'user_id':self.request.user.id,

                        'full_name':full_name,
                        'email_address':email_address,
                        'phone_number':phone_number,
                        'street_address1':street_address1,
                        'town_or_city':town_or_city,
                        'country_state_or_location':country_state_or_location,
                        'post_code':post_code,
                        'country':country,





                },
                mode='payment',
                success_url='http://{}{}'.format(host, reverse('profile')),
                cancel_url='http://{}{}'.format(host, reverse('shoping_cart')),
            )


            return redirect(checkout_session.url)











class signup(View):
    def get(self, request):
        register_form = forms.RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'signup.html', context)



    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['name']
        email = body['email']
        phone_number = body['phone_number']
        password = body['password']


        user: bool = models.User.objects.filter(email__iexact=email ).exists()
        user_namee: bool = models.User.objects.filter(username__exact=name).exists()
        if user:
               return JsonResponse({
                   'status': 'exist',
                   'message' :'email is exist!'
               })
        elif user_namee:
            return JsonResponse({
                'status': 'user exist' ,
                  'message' :'username is exist!'
            })

        else:
            new_user = models.User(
                     email=email,
                   email_active_code=get_random_string(72),
                    is_active=False,
                    username=name,
                    phone_number=phone_number
                )
            new_user.set_password(password)
            new_user.save()

            send_email('active account', new_user.email, {'user': new_user}, 'email_part/activate_account.html')
            return JsonResponse({
                'status': 'send',
                'message': 'email active code sent to to your email :)'
            })





class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user = models.User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()

                return redirect(reverse('login_page'))
            else:
                return redirect(reverse('home_pgae'))
                pass

        raise Http404




class LoginView(View):
    def get(self, request):
        login_form = forms.LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'login.html', context)

    def post(self, request ):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user = models.User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', ' your account is not active yet check your email.')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('profile'))
                    else:
                        login_form.add_error('email', 'password is wrong.')
            else:
                login_form.add_error('email', ' cant find user with this detail. ')

        context = {
            'login_form': login_form
        }

        return render(request, 'login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))





class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = forms.ForgotPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'forget_password.html', context)

    def post(self, request):
        forget_pass_form = forms.ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user = models.User.objects.filter(email__iexact=user_email).first()

            if user is None:
                forget_pass_form.add_error('email', 'email is not correct.')

            if user is not None:
                send_email(' reset password', user.email, {'user': user}, 'email_part/forgot_password.html')
                return redirect(reverse('home_pgae'))

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'forget_password.html', context)





class ResetPasswordView(View):
    def get(self, request, active_code):
        user= models.User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_pass_form = forms.ResetPasswordForm()

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'reset_password.html', context)

    def post(self, request, active_code):
        reset_pass_form = forms.ResetPasswordForm(request.POST)
        user = models.User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'reset_password.html', context)



def favorit(request,pk):

    if request.user.is_authenticated:
            post = get_object_or_404(Products, id=pk)
            fav = False
            if post.favorit.filter(id=request.user.id).exists():
                post.favorit.remove(request.user)
                fav = False
                return redirect('profile')
            else:
                post.favorit.add(request.user)
                fav = True

                return redirect('profile')



    else:

        return redirect('login_page')





def sendd_email(request):

    teller=models.News_teller.objects.all()
    for i in teller:
        try:
            send_email('new product', i.email, {'news': teller}, 'news_teller.html')
            return JsonResponse({
            'status': 'send',
            'message': 'email send successfully'

             })
        except:
            return JsonResponse({
                'status': 'not',
                'message': 'email can not send maybe there is no email to send!'

            })






def modify_order_detail(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['pk']



    m = models.OrderDetail.objects.filter(pk=pk, order__userr_id=request.user.id)
   
    m.delete()
    return JsonResponse({
        'status':'del',
        'message':'delete successfully'
    })



def remove_fav(request,pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Products, id=pk)
        liked = False
        if post.favorit.filter(id=request.user.id).exists():
            post.favorit.remove(request.user)
            liked = False
        return HttpResponseRedirect(reverse('profile'))
    else:
        return render(reverse('home_page'))



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
from order_module.forms import order_detail_form 
from order_module.models import OrderDetail ,Order ,order_data
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
        final_order =OrderDetail.objects.filter(order__is_paid=True, order__userr=self.request.user)

        fav=models.Products.objects.filter(favorit=self.request.user.id)
        user=models.User.objects.filter(id=self.request.user.id).first()
        delivary_data= order_data.objects.filter()

        context={
            'order':final_order,
            'fav':fav,
            'user':user,

            'delivary_data':delivary_data
        }



        return render(request,'profile.html',context)





class Edit_profilr(UpdateView):
        template_name = 'edit_user_detail.html'
        model =  User
        fields = ['first_name','last_name','email','username','phone_number']

        success_url = 'profile'


        def get_success_url(self):
            return reverse('profile')










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
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['user_email']
        
       
        
        user = models.User.objects.filter(email__iexact=email).first()
        
        print(user)
        

        if user is None:
            return JsonResponse({
                'status':'user_not_exist',
                'message':'email is not correct ot not register'
                })

        if user is not None:
            try:
                send_email(' reset password', user.email, {'user': user}, 'email_part/forgot_password.html')
                print('awe')
                return JsonResponse({
                    'status':'ok',
                    'message':'check your email for reset password'
                    })
            except:
                return JsonResponse({
                 'status':'error',
                 'message':'an error has occured'
                 })
            
        else:
            return JsonResponse({
                 'status':'error',
                 'message':'an error has occured'
                 })
            






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



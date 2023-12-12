from django.http import Http404 ,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from . import forms
from . import models
from django.utils.crypto import get_random_string
from .utils.email_service import send_email
from django.contrib.auth import login, logout
from main_module.models import Products
from main_module import models
import json



class Profile(TemplateView):


    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
         context = super(Profile, self).get_context_data()
         current_order, created = models.Order.objects.get_or_create(is_paid=False, userr_id=self.request.user.id)
         total_amount = 0
         for order_detail in current_order.orderdetail_set.all():
             total_amount += order_detail.product.price * order_detail.count

         context['order'] = current_order
         context['sum'] = total_amount
         context['fav']=models.Products.objects.filter(favorit=self.request.user.id)


         return context


class signup(View):
    def get(self, request):
        register_form = forms.RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'signup.html', context)



    def post(self, request):
        register_form =forms.RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user_name = register_form.cleaned_data.get('name')
            user_phone_number = register_form.cleaned_data.get('phone_number')
            user: bool = models.User.objects.filter(email__iexact=user_email ).exists()
            user_namee: bool = models.User.objects.filter(username__exact=user_name).exists()
            if user:
                register_form.add_error('email', 'email is exists')
            elif user_namee:
                register_form.add_error('name', 'name  is exist')

            else:
                new_user = models.User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_name,
                    phone_number=user_phone_number
                )
                new_user.set_password(user_password)
                new_user.save()



                send_email('active account', new_user.email, {'user': new_user}, 'email_part/activate_account.html')
                return redirect(reverse('home_pgae'))

        context = {
            'register_form': register_form
        }

        return render(request, 'signup.html', context)



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


    m = models.OrderDetail.objects.filter(product_id=pk, order__userr_id=request.user.id)
   
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



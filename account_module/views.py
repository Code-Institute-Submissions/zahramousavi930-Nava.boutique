from django.shortcuts import render,redirect,reverse,Http404
from django.views import View
from . import forms
from . import models
from django.utils.crypto import get_random_string
from .utils.email_service import send_email
from django.contrib.auth import login, logout

# Create your views here.

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
            if user is not None:
                send_email(' reset password', user.email, {'user': user}, 'email_part/forgot_password.html')
                return redirect(reverse('home_pgae'))

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'forget_password.html', context)


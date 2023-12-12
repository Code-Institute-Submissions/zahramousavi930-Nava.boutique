from django.shortcuts import render,redirect,reverse,Http404
from django.views import View
from . import forms
from . import models
from django.utils.crypto import get_random_string
from .utils.email_service import send_email


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


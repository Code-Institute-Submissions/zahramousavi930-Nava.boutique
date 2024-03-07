from django.test import TestCase
from .forms import RegisterForm,LoginForm,ResetPasswordForm,ForgotPasswordForm
# Create your tests here.


# class Testform(TestCase):

#     def test_requierd(self):
#         form =RegisterForm({'phone_number': '','email':'','name':'','password':''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('email',form.errors.keys())
#         self.assertIn('phone_number',form.errors.keys())
#         self.assertIn('name',form.errors.keys())
#         self.assertIn('password',form.errors.keys())
#         self.assertEqual(form.errors['email'][0],'This field is required.')
#         self.assertEqual(form.errors['phone_number'][0],'This field is required.')
#         self.assertEqual(form.errors['name'][0],'This field is required.')
#         self.assertEqual(form.errors['password'][0],'This field is required.')

#     def test_requierd_contact(self):
#         form = LoginForm({'email': '','password':''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('email', form.errors.keys())
#         self.assertIn('password', form.errors.keys())
#         self.assertEqual(form.errors['email'][0], 'This field is required.')
#         self.assertEqual(form.errors['password'][0], 'This field is required.')


#     def test_requierd_contact(self):
#         form = ResetPasswordForm({'password': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('password', form.errors.keys())
#         self.assertEqual(form.errors['password'][0], 'This field is required.')


#     def test_requierd_contact(self):
#         form = ForgotPasswordForm({'email': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('email', form.errors.keys())

#         self.assertEqual(form.errors['email'][0], 'This field is required.')

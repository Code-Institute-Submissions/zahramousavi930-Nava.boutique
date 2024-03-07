from django.test import TestCase
from . import forms
from . import models
from . import views



class CommentsFormTest(TestCase):

    def test_comments_form_valid_data(self):
        form_data = {
            'email': 'test@example.com',
            'text': 'This is a test comment.'
        }
        form = forms.comments(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comments_form_invalid_data(self):
        form_data = {
            'email': 'invalidemail', 
            'text': ''  
        }
        form = forms.comments(data=form_data)
        self.assertFalse(form.is_valid())

    def test_comments_form_save(self):
        form_data = {
            'email': 'test@example.com',
            'text': 'This is a test comment.'
        }
        form = forms.comments(data=form_data)
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        self.assertEqual(comment.email, 'test@example.com')
        self.assertEqual(comment.text, 'This is a test comment.')




class ContactFormTest(TestCase):

    def test_contact_form_valid_data(self):
        form_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'text': 'This is a test message.'
        }
        form = forms.contact_form(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        form_data = {
            'email': 'invalidemail', 
            'name': '',  
            'text': ''  
        }
        form = forms.contact_form(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_form_save(self):
        form_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'text': 'This is a test message.'
        }
        form = forms.contact_form(data=form_data)
        self.assertTrue(form.is_valid())
        contact_instance = form.save(commit=False)
        self.assertEqual(contact_instance.email, 'test@example.com')
        self.assertEqual(contact_instance.name, 'Test User')
        self.assertEqual(contact_instance.text, 'This is a test message.')




class OrderDetailFormTest(TestCase):

    def test_order_detail_form_valid_data(self):
        form_data = {
            'full_name': 'John Doe',
            'email_address': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'town_or_city': 'Anytown',
            'country_state_or_location': 'Some State',
            'post_code': '12345',
            'country': 'US'
        }
        form = forms.order_detail_form(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_detail_form_invalid_data(self):
        form_data = {
            'full_name': '', 
            'email_address': 'invalidemail', 
            'phone_number': '123',  
            'street_address1': '', 
            'town_or_city': '', 
            'country_state_or_location': '', 
            'post_code': '', 
            'country': ''  
        }
        form = forms.order_detail_form(data=form_data)
        self.assertFalse(form.is_valid())

    def test_order_detail_form_save(self):
        form_data = {
            'full_name': 'John Doe',
            'email_address': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'town_or_city': 'Anytown',
            'country_state_or_location': 'Some State',
            'post_code': '12345',
            'country': 'US'
        }
        form = forms.order_detail_form(data=form_data)
        self.assertTrue(form.is_valid())
        order_instance = form.save(commit=False)
        self.assertEqual(order_instance.full_name, 'John Doe')
        self.assertEqual(order_instance.email_address, 'john@example.com')
        self.assertEqual(order_instance.phone_number, '1234567890')
        self.assertEqual(order_instance.street_address1, '123 Main St')
        self.assertEqual(order_instance.town_or_city, 'Anytown')
        self.assertEqual(order_instance.country_state_or_location, 'Some State')
        self.assertEqual(order_instance.post_code, '12345')
        self.assertEqual(order_instance.country, 'US')











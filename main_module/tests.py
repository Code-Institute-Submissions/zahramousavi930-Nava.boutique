import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import FileSystemStorage
from account_module.models import User 
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



class CategoryModelTest(TestCase):

    def setUp(self):
        self.storage = FileSystemStorage(location='/workspace/Nava.boutique/img/comment.png')
        self.storage.location = '/workspace/Nava.boutique/img'

    def tearDown(self):
        self.storage.delete('category/test_image.jpg')

    def test_category_str_representation(self):
        category = models.Category(categoryy='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_category_parent_is_null(self):
        category =  models.Category.objects.create(categoryy='Parent Category')
        self.assertIsNone(category.parent)

    def test_category_has_parent(self):
        parent_category =  models.Category.objects.create(categoryy='Parent Category')
        child_category =  models.Category.objects.create(categoryy='Child Category', parent=parent_category)
        self.assertEqual(child_category.parent, parent_category)

   


class ProductsModelTest(TestCase):

    def test_products_str_representation(self):
        product = models.Products(name='Test Product', price=100)
        self.assertEqual(str(product), 'Test Product')

    def test_products_creation(self):
        category = models.Category.objects.create(categoryy='Test Category')
        product = models.Products.objects.create(
            name='Test Product',
            slug='test-product',
            category=category,
            price=100,
            size='Large',
            description='Test description',
            image='/workspace/Nava.boutique/img/products.png',  
            color='Red',
            color2='Blue',
        )
        
        
        self.assertIsNotNone(product)

        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(product.category, category)
        self.assertEqual(product.price, 100)
        self.assertEqual(product.size, 'Large')
        self.assertEqual(product.description, 'Test description')
        self.assertEqual(product.image, '/workspace/Nava.boutique/img/products.png')
        self.assertEqual(product.color, 'Red')
        self.assertEqual(product.color2, 'Blue')





class NewsTellerModelTest(TestCase):

    def test_news_teller_creation(self):
        email = 'test@example.com'
        news_teller = models.News_teller.objects.create(email=email)
        
       
        self.assertIsNotNone(news_teller)

        
        self.assertEqual(news_teller.email, email)

    def test_news_teller_str_representation(self):
        email = 'test@example.com'
        news_teller =  models.News_teller.objects.create(email=email)
        
        
        self.assertEqual(str(news_teller), email)




class AddCommentsModelTest(TestCase):

    def test_add_comments_str_representation(self):
        user = User.objects.create(username='test_user')
        product = models.Products.objects.create(name='Test Product', price=100)
        comment = models.add_comments.objects.create(
            product=product,
            user=user,
            email='test@example.com',
            text='Test comment',
        )

     
        expected_str = str(user)
        self.assertEqual(str(comment), expected_str)

    def test_add_comments_creation(self):
        user = User.objects.create(username='test_user')
        product = models.Products.objects.create(name='Test Product', price=100)
        comment = models.add_comments.objects.create(
            product=product,
            user=user,
            email='test@example.com',
            text='Test comment',
        )

       
        self.assertIsNotNone(comment)

  
        self.assertEqual(comment.product, product)
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.email, 'test@example.com')
        self.assertEqual(comment.text, 'Test comment')




class ContactWithUsModelTest(TestCase):

    def test_contact_with_us_str_representation(self):
        contact = models.contact_with_us.objects.create(
            email='test@example.com',
            phone_number='123456789',
            about_us='Test message about us.',
        )

       
        expected_str = 'test@example.com'
        self.assertEqual(str(contact), expected_str)

    def test_contact_with_us_creation(self):
        contact = models.contact_with_us.objects.create(
            email='test@example.com',
            phone_number='123456789',
            about_us='Test message about us.',
        )

        
        self.assertIsNotNone(contact)

      
        self.assertEqual(contact.email, 'test@example.com')
        self.assertEqual(contact.phone_number, '123456789')
        self.assertEqual(contact.about_us, 'Test message about us.')




class ContactModelTest(TestCase):

    def test_contact_str_representation(self):
        email = 'test@example.com'
        name = 'Test User'
        text = 'Test message'
        contact_instance = models.contact.objects.create(email=email, name=name, text=text)

  
        expected_str = email
        self.assertEqual(str(contact_instance), expected_str)

    def test_contact_creation(self):
        email = 'test@example.com'
        name = 'Test User'
        text = 'Test message'
        contact_instance =  models.contact.objects.create(email=email, name=name, text=text)

      
        self.assertIsNotNone(contact_instance)

    
        self.assertEqual(contact_instance.email, email)
        self.assertEqual(contact_instance.name, name)
        self.assertEqual(contact_instance.text, text)




class ContactModelTest(TestCase):

    def test_contact_str_representation(self):

        contact_us = models.contact.objects.create(email='test@example.com', name='Test User', text='This is a test message')

        expected_str = 'test@example.com'
        self.assertEqual(str(contact_us), expected_str)





class OrderModelTest(TestCase):

    def test_order_str_representation(self):
       
        user = User.objects.create(username='test_user')

     
        order = models.Order.objects.create(userr=user, is_paid=False)

      
        expected_str = str(user)
        self.assertEqual(str(order), expected_str)

    def test_order_payment_date_is_none(self):
      
        user = User.objects.create(username='test_user')

        order = models.Order.objects.create(userr=user, is_paid=True, payment_date=None)

        self.assertIsNone(order.payment_date)

    def test_order_payment_date_is_not_none(self):
  
        user = User.objects.create(username='test_user')

        payment_date = '2024-03-07 12:00:00'

        order = models.Order.objects.create(userr=user, is_paid=True, payment_date=payment_date)

        self.assertEqual(str(order.payment_date), payment_date)






class OrderDetailModelTest(TestCase):

    def test_order_detail_order_str_representation(self):

        user = User.objects.create(username='test_user')

        order = models.Order.objects.create(userr=user, is_paid=False)

        order_detail = models.OrderDetail.objects.create(order=order) 
        expected_str = str(user)
        self.assertEqual(str(order_detail.order), expected_str)

    def test_order_detail_product_str_representation(self):

        user = User.objects.create(username='test_user')


        order = models.Order.objects.create(userr=user, is_paid=False)


        product = models.Products.objects.create(name='Test Product', price=100)

        order_detail = models.OrderDetail.objects.create(order=order, product=product)

        expected_str = 'Test Product'
        self.assertEqual(str(order_detail.product), expected_str)
     

    def test_order_detail_default_values(self):
  
        user = User.objects.create(username='test_user')

      
        order = models.Order.objects.create(userr=user, is_paid=False)

       
        order_detail = models.OrderDetail.objects.create(order=order)

     
        self.assertEqual(order_detail.size, '')
        self.assertEqual(order_detail.color, '')
        self.assertEqual(order_detail.count, 1)
        self.assertEqual(order_detail.order_number, 0)
        self.assertIsNone(order_detail.final_price)







class OrderDataModelTest(TestCase):

    def setUp(self):
     
        self.user = User.objects.create(username='test_user', email='test@example.com')

     
        self.order = models.Order.objects.create(userr=self.user, is_paid=False)

      
        self.product = models.Products.objects.create(name='Test Product', slug='test-product', price=100)

       
        self.order_detail = models.OrderDetail.objects.create(
            order=self.order,
            product=self.product,
            final_price='100',
            count=2
        )
    def test_order_data_str_representation(self):
        order = models.order_data.objects.create(
            full_name='Test User',
            email_address='test@example.com',
            phone_number='123456789',
            street_address1='123 Test St',
            town_or_city='Test City',
            country_state_or_location='Test Country',
            post_code='12345',
            country='Test Country',
        
            which_user=self.user
        )

        self.assertEqual(str(order), 'test@example.com')

    def test_order_data_has_order_detail(self):
        order = models.order_data.objects.create(
            full_name='Test User',
            email_address='test@example.com',
            phone_number='123456789',
            street_address1='123 Test St',
            town_or_city='Test City',
            country_state_or_location='Test Country',
            post_code='12345',
            country='Test Country',
            which_user=self.user
        )
        order.which_order.add(self.order_detail)

        self.assertEqual(order.which_order.count(), 1)
        self.assertIn(self.order_detail, order.which_order.all())





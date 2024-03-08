from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import FileSystemStorage
from django.test import TestCase, Client, RequestFactory
from account_module.models import User
from django.urls import reverse, reverse_lazy
from . import forms
from . import models
from . import views
import json
import os


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



class CategoryModelTest(TestCase):

    def setUp(self):
        self.storage = FileSystemStorage(
            location='/workspace/Nava.boutique/img/comment.png')
        self.storage.location = '/workspace/Nava.boutique/img'

    def tearDown(self):
        self.storage.delete('category/test_image.jpg')

    def test_category_str_representation(self):
        category = models.Category(categoryy='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_category_parent_is_null(self):
        category = models.Category.objects.create(categoryy='Parent Category')
        self.assertIsNone(category.parent)

    def test_category_has_parent(self):
        parent_category = models.Category.objects.create(
            categoryy='Parent Category')
        child_category = models.Category.objects.create(
            categoryy='Child Category', parent=parent_category)
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
        self.assertEqual(
            product.image, '/workspace/Nava.boutique/img/products.png')
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
        news_teller = models.News_teller.objects.create(email=email)

        self.assertEqual(str(news_teller), email)


class AddCommentsModelTest(TestCase):

    def test_add_comments_str_representation(self):
        user = User.objects.create(username='test_user')
        product = models.Products.objects.create(
            name='Test Product', price=100)
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
        product = models.Products.objects.create(
            name='Test Product', price=100)
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
        contact_instance = models.contact.objects.create(
            email=email, name=name, text=text)

        expected_str = email
        self.assertEqual(str(contact_instance), expected_str)

    def test_contact_creation(self):
        email = 'test@example.com'
        name = 'Test User'
        text = 'Test message'
        contact_instance = models.contact.objects.create(
            email=email, name=name, text=text)

        self.assertIsNotNone(contact_instance)

        self.assertEqual(contact_instance.email, email)
        self.assertEqual(contact_instance.name, name)
        self.assertEqual(contact_instance.text, text)


class ContactModelTest(TestCase):

    def test_contact_str_representation(self):

        contact_us = models.contact.objects.create(
            email='test@example.com', name='Test User', text='This is a test message')

        expected_str = 'test@example.com'
        self.assertEqual(str(contact_us), expected_str)














# views test

class SearchViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username='testuser', password='password')

    def test_search_view(self):

        product = models.Products.objects.create(
            name='Test Product',
            slug='test-product',
            price=100,
            description='Test description',
            image='test_image.jpg'
        )

        data = {'search': 'Test'}
        request = self.factory.post(reverse('search'), data)

        request.user = self.user

        response = views.search(request)

        self.assertEqual(response.status_code, 200)

        self.assertIn(product.name.encode(), response.content)



class SaveContactUsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_save_contact_us(self):
        
        post_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'text': 'Test message for contact form.'
        }


        request = self.factory.post(reverse('save_contact'), post_data)

    
        response = views.save_contact_us(request)


        self.assertEqual(response.url, reverse('home_pgae'))

       
        contact = models.contact.objects.last()
        self.assertEqual(contact.name, post_data['name'])
        self.assertEqual(contact.email, post_data['email'])
        self.assertEqual(contact.text, post_data['text'])

    def test_save_contact_us_invalid_request(self):
     
        request = self.factory.get(reverse('save_contact'))

     
        response = views.save_contact_us(request)

     
        self.assertEqual(response.url, reverse('home_pgae'))




class AddCommentsPartTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_comments_authenticated(self):
        product = models.Products.objects.create(name='Test Product', slug='test-product', price=100)
        user = User.objects.create(username='testuser')

        request = self.factory.post(reverse('add_comments'), json.dumps({
            'id': product.id,
            'text': 'Test comment',
            'email': 'test@example.com',
            'rate': 4
        }), content_type='application/json')
        request.user = user

        response = views.add_comments_part(request)

        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['status'], 'ok')
        self.assertEqual(content['message'], 'refresh page to see your comment.')



class ProductsDetailViewTest(TestCase):
    def test_products_detail_view(self):
        product = models.Products.objects.create(name='Test Product', slug='test-product', price=100)

        client = Client()
        response = client.get(reverse('products_pgae', kwargs={'slug': 'test-product', 'pk': product.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')




class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
     
        cls.parent_category = models.Category.objects.create(categoryy="Parent Category")
       
        cls.category_with_parent = models.Category.objects.create(categoryy="Child Category", parent=cls.parent_category)
       
        cls.category_without_parent = models.Category.objects.create(categoryy="Top Level Category")

    def test_category_str_method(self):
        
        self.assertEqual(str(self.parent_category), self.parent_category.categoryy)
        self.assertEqual(str(self.category_with_parent), self.category_with_parent.categoryy)
        self.assertEqual(str(self.category_without_parent), self.category_without_parent.categoryy)

    def test_parent_category_relationship(self):
     
        self.assertEqual(self.category_with_parent.parent, self.parent_category)

    def test_blank_and_null_fields(self):

        self.assertIsNone(self.category_without_parent.parent)
        self.assertEqual(self.category_without_parent.image, '')  




class RemoveNewsTellerViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
    def test_remove_news_teller(self):
       
        email = 'test@example.com'
        news_teller = models.News_teller.objects.create(email=email)

        
        data = {'removenewstelleremail': email}
        request = self.factory.post(reverse('remove_news_teller'), data)

        
        response = views.remove_news_teller(request)

     
        self.assertEqual(models.News_teller.objects.count(), 0)

       
        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, reverse('home_pgae'))


class NewsTellerViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_newsteller_view(self):
     
        data = {'newstelleremail': 'test@example.com'}
        request = self.factory.post(reverse('news_teller'), data)

        
        response = views.newsteller(request)

     
        self.assertEqual(models.News_teller.objects.count(), 1)
        news_teller = models.News_teller.objects.first()
        self.assertEqual(news_teller.email, 'test@example.com')

       
        self.assertEqual(response.status_code, 302)

        
        self.assertEqual(response.url, reverse('home_pgae'))



class HomePageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser', password='12345')
        category = models.Category.objects.create(categoryy='Test Category')
        models.Products.objects.create(name='Test Product', slug='test-product', category=category, price=100)

    def test_home_page_view(self):
        response = self.client.get(reverse('home_pgae'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')
        self.assertTrue('products_discount' in response.context)
        self.assertTrue('products' in response.context)
        self.assertTrue('category' in response.context)











class ContactWithUsViewTest(TestCase):
    def setUp(self):
        self.contact_info = models.contact_with_us.objects.create(
            email='test@example.com',
            phone_number='1234567890',
            about_us='Test about us text'
        )

    def test_contact_with_us_view(self):
        client = Client()
        response = client.get(reverse('contact_with_us'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'contac_with_us.html')

        self.assertQuerysetEqual(response.context['footer'], models.contact_with_us.objects.all())





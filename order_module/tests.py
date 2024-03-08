from django.test import TestCase ,RequestFactory
from . import views 
from . import models
from . import forms
from django.urls import reverse
import json
from account_module.models import User


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
        self.assertEqual(
            order_instance.country_state_or_location, 'Some State')
        self.assertEqual(order_instance.post_code, '12345')
        self.assertEqual(order_instance.country, 'US')




class AddToCartViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_to_cart_authenticated(self):

        user = models.User.objects.create_user(
            username='testuser', password='12345')

        product = models.Products.objects.create(
            name='Test Product', slug='test-product', price=100)

        request = self.factory.post(reverse('add_to_cart'), json.dumps({
            'pk': product.pk,
            'size': 'small',
            'color': 'red',
            'count': 1
        }), content_type='application/json')
        request.user = user

        response = views.addtocart(request)

        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['status'], 'success')
        self.assertEqual(content['message'], 'order add to cart')



class OrderModelTest(TestCase):

    def test_order_str_representation(self):

        user = User.objects.create(username='test_user')

        order = models.Order.objects.create(userr=user, is_paid=False)

        expected_str = str(user)
        self.assertEqual(str(order), expected_str)

    def test_order_payment_date_is_none(self):

        user = User.objects.create(username='test_user')

        order = models.Order.objects.create(
            userr=user, is_paid=True, payment_date=None)

        self.assertIsNone(order.payment_date)

    def test_order_payment_date_is_not_none(self):

        user = User.objects.create(username='test_user')

        payment_date = '2024-03-07 12:00:00'

        order = models.Order.objects.create(
            userr=user, is_paid=True, payment_date=payment_date)

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

        product = models.Products.objects.create(
            name='Test Product', price=100)

        order_detail = models.OrderDetail.objects.create(
            order=order, product=product)

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

        self.user = User.objects.create(
            username='test_user', email='test@example.com')

        self.order = models.Order.objects.create(
            userr=self.user, is_paid=False)

        self.product = models.Products.objects.create(
            name='Test Product', slug='test-product', price=100)

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


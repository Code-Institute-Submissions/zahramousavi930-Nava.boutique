from django.test import TestCase
from .forms import comments ,contact_form
from . import models
# Create your tests here.

class Testform(TestCase):

    def test_requierd(self):
        form =comments({'email': '','text':''})
        self.assertFalse(form.is_valid())
        self.assertIn('email',form.errors.keys())
        self.assertIn('text',form.errors.keys())
        self.assertEqual(form.errors['email'][0],'This field is required.')
        self.assertEqual(form.errors['text'][0],'This field is required.')

    def test_requierd_contact(self):
        form = contact_form({'email': '','name':'','text':''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertIn('text', form.errors.keys())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertEqual(form.errors['text'][0], 'This field is required.')
        self.assertEqual(form.errors['name'][0], 'This field is required.')



class Test_views(TestCase):
    def test_get_home(self):
        response =self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home_page.html')

    def test_get_category(self):
        response =self.client.get('/category/2')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'category_products.html')


    def test_get_all_products(self):
        response =self.client.get('/all')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'all products.html')




class Test_name_models(TestCase):
    def test_str(self):
        item = models.contact.objects.create(email='test@email.com')
        self.assertEqual(str(item),'test@email.com')

        item1 = models.Products.objects.create(name='shirt',slug='shirt',price=22,size=12,description='erfas')
        self.assertEqual(str(item1), 'shirt')

        item2 = models.News_teller.objects.create(email='test@email.com')
        self.assertEqual(str(item2), 'test@email.com')

        item3 = models.Category.objects.create(categoryy='man')
        self.assertEqual(str(item3), 'man')



        item5 = models.contact_with_us.objects.create(email='test@email.com')
        self.assertEqual(str(item5), 'test@email.com')



class test_models(TestCase):
    def defualt_fasle_Products(self):
        item=models.Products.objects.create(name='wqe')
        self.assertFalse(item.done)

    def defualt_fasle_order(self):
        item2 = models.Order.objects.create(userr='lkewrt')
        self.assertFalse(item2.done)

    def defualt_fasle_OrderDetail(self):
        item3 = models.OrderDetail.objects.create(order='weae')
        self.assertFalse(item3.done)

    def defualt_fasle_contact_with_us(self):
        item4 = models.contact_with_us.objects.create(email='awoeka@gmail.com')
        self.assertFalse(item4.done)

    def defualt_fasle_add_comments(self):
        item4 = models.add_comments.objects.create(email='awoeka@gmail.com')
        self.assertFalse(item4.done)

    def defualt_fasle_News_teller(self):
        item4 = models.News_teller.objects.create(email='awoeka@gmail.com')
        self.assertFalse(item4.done)





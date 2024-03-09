from django.shortcuts import render
from django.http import Http404 ,HttpResponseRedirect,JsonResponse,HttpResponse
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views import View
from . import models
from  account_module.utils.email_service import send_email
from .models import Products
from .forms import order_detail_form
import json
from NovaBoutique import settings
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from account_module.models import User
import random


class Shoping_cart(View):
    def get(self,request):
         current_order, created = models.Order.objects.get_or_create(is_paid=False, userr_id=self.request.user.id)

         total_amount = 0
         for order_detail in current_order.orderdetail_set.all():
              total_amount += order_detail.product.price * order_detail.count



         context={
             'order_form':order_detail_form(),
             'order':current_order,
             'sum':total_amount
         }

         return render(request ,'shoping_cart.html',context)

    def post(self,request):
        if request.POST:
            current_order, created = models.Order.objects.get_or_create(is_paid=False, userr_id=self.request.user.id)
            order_detail_id = models.OrderDetail.objects.filter(final_price=None, order__userr=self.request.user.id)


            total_amount = 0
            products_name =[]
            for order_detail in current_order.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
                products_name.append(order_detail.product.name)

            full_name = request.POST.get('full_name')
            email_address = request.POST.get('email_address')
            phone_number = request.POST.get('phone_number')
            street_address1 = request.POST.get('street_address1')
            town_or_city = request.POST.get('town_or_city')
            country_state_or_location = request.POST.get('country_state_or_location')
            post_code = request.POST.get('post_code')
            country = request.POST.get('country')

            stripe.api_key = settings.STRIPE_SECRET_KEY
            host = self.request.get_host()
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': '{}'.format(total_amount * 100),
                            'product_data': {
                             'name':'Nova'

                            },
                        },
                        'quantity': 1,
                    },
                ],
                metadata={
                    'user_id':self.request.user.id,

                        'full_name':full_name,
                        'email_address':email_address,
                        'phone_number':phone_number,
                        'street_address1':street_address1,
                        'town_or_city':town_or_city,
                        'country_state_or_location':country_state_or_location,
                        'post_code':post_code,
                        'country':country,





                },
                mode='payment',
                success_url='https://nova-123-90e80f3300ba.herokuapp.com/user/profile',
                cancel_url='https://nova-123-90e80f3300ba.herokuapp.com/order/shoping-cart',
            )


            return redirect(checkout_session.url)




@csrf_exempt
def stripe_webhook(request):
        # payload = request.body
        payload = request.body.decode('utf-8')
        sig_header =request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except ValueError as e:
            return HttpResponse(status=400)
            
        except stripe.error.SignatureVerificationError as e:

            
            return HttpResponse(status=400)

        if event['type'] == 'checkout.session.completed':
            amount = event['data']['object']
            user_id = amount['metadata']['user_id']
            total=amount['amount_total']

            full_name = amount['metadata']['full_name']
            email_address = amount['metadata']['email_address']
            phone_number = amount['metadata']['phone_number']
            street_address1 = amount['metadata']['street_address1']
            town_or_city = amount['metadata']['town_or_city']
            country_state_or_location = amount['metadata']['country_state_or_location']
            post_code = amount['metadata']['post_code']
            country = amount['metadata']['country']







            order_basket=models.Order.objects.filter(is_paid=False,userr_id=user_id).all()

            for order in order_basket:
                if order.is_paid == False:
                     order.is_paid = True
                     order.payment_date =timezone.now()


                     order.save()

                if order.payment_date == None:
                    order.delete()
                    order.save()




            order_detail_final_price=models.OrderDetail.objects.filter(final_price=None,order__userr=user_id).all()
            total_price='{}'.format(total)[:-2]
            for orders in order_detail_final_price:
                if orders.final_price == None:
                    orders.final_price = total_price
                    orders.save()





            user=models.User.objects.filter(id=user_id).first()





            new_data=models.order_data(
                full_name=full_name,
                email_address=email_address,
                phone_number=phone_number,
                street_address1=street_address1,
                town_or_city=town_or_city,
                country_state_or_location=country_state_or_location,
                post_code=post_code,
                country=country,
                which_user=user

            )
            new_data.save()
            for orderss in order_detail_final_price:
                new_data.which_order.add(orderss)



            main_email=email_address


            send_email('new order', main_email, {'order_basket': order_detail_final_price,'date':new_data,}, 'email_part/order.html')


        return HttpResponse(status=200)



def detailcart(request,pk):

    detail=models.order_data.objects.filter(which_order=pk).get()
    payment_datea=models.OrderDetail.objects.filter(pk=pk).get()

    return render(request,'detailcart.html',{'detail':detail,'payment_datea':payment_datea})





def addtocart(request):
    data = json.loads(request.body.decode("utf-8"))
    pk = data['pk']
    sizee = data['size']
    colorr = data['color']
    count = data['count']




    if request.user.is_authenticated:
        product = models.Products.objects.filter(id=pk).first()
        random_numbers = [random.randint(1, 100) for _ in range(3)]
        formatted_numbers2 = ''.join(map(str, random_numbers))
        if product is not None:
             current_order, created = models.Order.objects.get_or_create(is_paid=False, userr_id=request.user.id)
             current_order_detail = current_order.orderdetail_set.filter(product_id=pk).first()

             if current_order_detail is not None:

                 new_detail = models.OrderDetail(order_id=current_order.id, product_id=pk, size=sizee, color=colorr,count=count,order_number=formatted_numbers2)
                 new_detail.save()
             else:
                 random_numbers = [random.randint(1, 100) for _ in range(3)]
                 formatted_numbers= ''.join(map(str, random_numbers))


                 new_detail =models.OrderDetail(order_id=current_order.id
                                               ,product_id=pk
                                               ,size=sizee,
                                               color=colorr,
                                               count=count,
                                                order_number=formatted_numbers
                                                )
                 new_detail.save()

             return JsonResponse({
                'status': 'success',
                'message':'order add to cart',

            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'message': 'product dose not exists',

            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'message': 'please login then order!',

        })





def modify_order_detail(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    pk = body['pk']



    m = models.OrderDetail.objects.filter(pk=pk, order__userr_id=request.user.id)
   
    m.delete()
    return JsonResponse({
        'status':'del',
        'message':'delete successfully'
    })

from django.http.response import JsonResponse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class CartView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        try:
            cart=Cart.objects.get(user=request.user)
            products=cart.products.all()
            data=[]

            for product in products:
                data.append({
                    'name':product.name,
                    'price':product.price,
                    'image':product.image,
                    'id':product.id
                })

            reply={'data':data,'success':True}
        except:
            reply = {'data': [], 'success': False}


        return JsonResponse(reply,safe=False)


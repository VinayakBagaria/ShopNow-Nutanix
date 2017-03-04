from django.views.generic import ListView,DetailView
from .models import *
from django.views import View
from cart.models import Cart
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


def get_products(query=None):
    data={}
    queryset=Product.objects.all()

    # only if a name is asked in the search field, then query the db for that name query.
    if query:
        queryset=queryset.filter(name__icontains=query)

    """
    Initially no data in product.category so cant append. Goes to except and inserts this data as a list. Next when this category is
    encountered, put the product in this list. So whenever a new category comes, except part is 1st called then try is done for each
    other iteration of the category.
    """
    for product in queryset:
        try:
            data[product.category].append(product)
        except KeyError:
            data[product.category]=[product]

    return [{'category':k,'products':v} for k,v in data.items()]


class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'products/list_view.html'

    def get_queryset(self):
        return get_products()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/one_product.html'


class ProductSearchView(ListView):
    model = Product
    template_name = 'products/list_view.html'

    def get_queryset(self):
        q=self.request.GET.get('q')
        return get_products(q)


class ProductCartView(LoginRequiredMixin,View):

    def post(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        product=Product.objects.get(pk=pk)

        try:
            cart=Cart.objects.get(user=request.user)
            cart.products.add(product)
            cart.save()
        except Cart.DoesNotExist:
            cart=Cart(user=request.user)
            cart.save()
            cart.products.add(product)
            cart.save()

        return JsonResponse({'success':True},safe=False)

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(product)
        cart.save()

        return JsonResponse({'success': True}, safe=False)
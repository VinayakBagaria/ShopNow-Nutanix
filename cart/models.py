from products.models import *
from django.contrib.auth.models import User

# each user has his own cart ; each user should see all the products
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product)

    def get_products(self):
        return ", ".join([p.name for p in self.products.all()])
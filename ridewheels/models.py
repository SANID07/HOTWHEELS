from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    password = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone=models.IntegerField()
    def __str__(self):
        return f"{self.name}"


class Feedback(models.Model):

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    email = models.EmailField()
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cars', 'Cars'),
        ('trucks', 'Trucks'),
        ('bikes', 'Bikes'),
        ('limited', 'Limited Edition'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    
    
class Cart(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.IntegerField(default=1)

def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')


class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


class Wishlist(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        product = models.ForeignKey('Product', on_delete=models.CASCADE)

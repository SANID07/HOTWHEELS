from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect



from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')




def about(request):
    return render(request,'about.html')

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

from .forms import FeedbackForm

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from .models import Feedback


def feedback_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')

        Feedback.objects.create(
            email=email,
            feedback_text=feedback_text,
            rating=rating
        )

        return redirect('thank_you')

    return render(request, 'feedback.html')

def logout(request):
    request.session.flush()
    return redirect('index')
from.models import *
from django.contrib import messages
def register(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       password = request.POST.get('password')
       address = request.POST.get('location')
       phone = request.POST.get('phone')
       if User.objects.filter(email=email).exists():
          messages.error(request, 'Email already registered.')
       else:
          User.objects.create(name=name, email=email, password=password, address=address, phone=phone)
          messages.success (request, 'Registration successful!')
          return redirect('index')
    return render (request, 'register.html')

def login(request):
   if request.method == 'POST':
         email = request.POST.get('email')
         password = request.POST.get('password')
         try:
            user = User.objects.get(email=email, password=password)
            request.session['email'] = user.email
            return redirect('home')
         except User. DoesNotExist:
            return render (request, 'login.html', {'error': 'Invalid email or password.'})
   return render (request, 'login.html')


def profile(request):
   email = request.session.get('email')

   if email is not None:
          try:
              user = User.objects.get(email=email)
              return render (request, 'profile.html', {'user': user})
          except User. DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('login')
   else:
          messages.warning (request, "You need to log in to access your profile.")
          return redirect('login')
   


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


# Product List

def product_list(request):

    products = Product.objects.all()

    return render(request, 'productlist.html', {'products': products})

def userproductlist(request):

    products = Product.objects.all()

    return render(request, 'userproductlist.html', {'products': products})

# Add Product

def add_product(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        stock = request.POST.get('stock')

        Product.objects.create(
            name=name,
            category=category,
            price=price,
            image=image,
            description=description,
            stock=stock
        )

        return redirect('product_list')

    return render(request, 'add_product.html')


# Edit Product

def edit_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':

        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.stock = request.POST.get('stock')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()

        return redirect('product_list')

    return render(request, 'editproduct.html', {'product': product})


# Delete Product

def delete_product(request, id):

    product = get_object_or_404(Product, id=id)

    product.delete()

    return redirect('product_list')


def adminhome(request):
    return render(request,'adminhome.html')

def adminlogin(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        u='admin'
        p='admin'
        if uname==u:
            if passw==p:
                return redirect('adminhome')
    return render(request,'adminlogin.html')




def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    email = request.session.get('email')

    if email:
        user = get_object_or_404(User, email=email)

        cart_item, created = Cart.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')
    else:
        return JsonResponse({'error': 'Login first'}, status=400)
    
def cart(request):
    email = request.session.get('email')

    if email:
        user = get_object_or_404(User, email=email)
        cart_items = Cart.objects.filter(user=user)

        for item in cart_items:
            item.total_price = item.product.price * item.quantity

        total_price = sum(item.total_price for item in cart_items)

        return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total_price': total_price
        })
    else:
        return render(request, 'cart.html', {
            'error': 'Login required'
        })
    
def delete_cart(request, id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=id)
        cart_item.delete()
        return redirect('cart')

    return redirect('cart')




def wishlist(request):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = get_object_or_404(User, email=email)
    items = Wishlist.objects.filter(user=user)

    return render(request, 'wishlist.html', {'items': items})


def add_to_wishlist(request, id):
    email = request.session.get('email')

    if not email:
        return redirect('login')

    user = get_object_or_404(User, email=email)
    product = get_object_or_404(Product, id=id)

    Wishlist.objects.get_or_create(
        user=user,
        product=product,
    )

    return redirect('wishlist')

def thank_you(request):
    return render(request, 'thank_you.html')

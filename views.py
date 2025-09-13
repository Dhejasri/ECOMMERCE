from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Product, ProductImage
from django.http import HttpResponse

cart=[]
favourites=[]
purchases=[]

def home(request):
    Ethnicwear = Product.objects.filter(category='EthnicWear')[:5]
    Westernwear = Product.objects.filter(category='WesternWear')[:5]
    footwears = Product.objects.filter(category='FootWears')[:5]
    electronics = Product.objects.filter(category='electronics')[:5]
    return render(request,'home.html',{
        'Ethnicwear': Ethnicwear,
        'Westernwear': Westernwear,
        'footwears': footwears,
        'electronics': electronics
        
    })

    
def about(request):
    return render(request, 'about.html')
 
def contact(request):
    return render(request, 'contact.html')

def product_detail(request,pid):
    product=get_object_or_404(Product,id=pid)
    return render(request,'product_detail.html',{'product':product})

def add_cart(request,pid):
    request.session.get('cart', [])
    cart.append(pid)
    request.session['cart'] = cart
    messages.success(request, "Item added to cart")
    return redirect('home')

def add_fav(request,pid):
    request.session.get('favourites', [])
    favourites.append(pid)
    request.session['favourites'] = favourites
    messages.info(request, "Items added to favourites")
    return redirect('home')

def purchase(request,pid):
    request.session.get('purchases', [])
    purchases.append(pid)
    request.session['purchases'] = purchases
    messages.success(request, "Purchse sucessfull")
    return redirect('home')

def product_gallery(request, pid):
    product = get_object_or_404(Product, id=pid)
    images = ProductImage.objects.filter(product=product)  
    return render(request, 'product_gallery.html', {
        'product': product,
        'images': images
    })

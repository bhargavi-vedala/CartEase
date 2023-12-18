from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from cartapp.models import Product,Review,Category,Cart,Buy
from cartapp.cartease import * 
from cartapp.forms import CartForm,ReviewForm
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Category
@login_required(login_url='/s/')  # Update the login URL
def category(request):
    if 'q' in request.GET:
        q=request.GET['q']
        c=Category.objects.filter(title__icontains=q)
    else:
        c = Category.objects.all()
    context = {'c': c}
    return render(request, 'index.html', context)


def products(request,product_id,slug):
    d=Product.objects.filter(category=product_id)
    context={'d':d}
    return render(request,'products.html',context)  
def detail(request,product_id,slug):
    d=Product.objects.get(id=product_id)
    reviews = Review.objects.filter(post_id = product_id)
    if request.method=="POST":
        f=CartForm(request,request.POST)
        if f.is_valid():
            request.form_data=f.cleaned_data
            add_to_cart(request)
            return redirect('cartapp:cart_view')

    f=CartForm(request,initial={'product_id':product_id})
    context={'d':d,'f':f,'reviews':reviews} 
    return render(request,'detail.html',context)
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('cartapp:category')
        else:
            messages.error(request,'Invalid user credentials')
            return redirect('cartapp:signin')
    else:
        return render(request,'signin.html')

def logout(request):
    auth.logout (request)
    return redirect('cartapp:home')
    return render(request,'home.html')    
def signup(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('cartapp:signup')

        otp_number = random.randint(1000, 9999)
        otp = str(otp_number)
        send_otp(email, otp)
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password
        request.session['otp'] = otp  # Add this line to store OTP in the session

        # Construct the URL using HttpResponseRedirect
        #return HttpResponseRedirect(f'/otp/{otp}/{username}/{password}/{email}/')
        # Alternatively, you can use reverse:
        return HttpResponseRedirect(reverse('cartapp:otp', args=[otp, username, password, email]))

    else:
        return render(request, 'signup.html')
    return render(request,'signup.html')
def send_otp(email, otp):
    subject = 'OTP Verification'
    message = f'Your OTP for cartapp is: {otp}'
    send_mail(subject, message, None, [email])

def cart_view(request):
    if request.method=="POST" and request.POST.get('delete')=='Delete':
        item_id=request.POST.get('item_id')
        cd=Cart.objects.get(id=item_id)
        cd.delete()
    c=get_cart(request)
    t=total_(request)
    co=item_count(request)
    context={'c':c,'t':t} 
    return render(request,'cart.html',context)      
def order(request):
    items=get_cart(request)
    for i in items:
        b=Buy(product_id=i.product_id,quantity=i.quantity,price=i.price)
        b.save()
    paypal_dict = {
        "business": "sb-fejqu28145983@business.example.com",
        "amount": total_(request),
        "item_name": cart_id(request),
        "invoice": str(uuid.uuid4()),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('cartapp:return_view')),
        "cancel_return": request.build_absolute_uri(reverse('cartapp:cancel_view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form,"items":items,"total":total_(request)}
    return render(request, "order.html", context)
def return_view(request):
    return render(request,'Transaction.html')
def cancel_view(request):
    return HttpResponse('Transaction Cancelled') 
def contact(request):
    return render(request,'contact.html') 
def otp(request, otp, username, password, email):
    if request.method == "POST":
        uotp = request.POST['otp']
        otp_from_session = request.session.get('otp')
        if uotp == otp_from_session:
            username = request.session.get('username')
            email = request.session.get('email')
            password = request.session.get('password')
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('cartapp:signin')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('cartapp:otp', otp=otp, username=username, password=password, email=email)

    return render(request, 'otp.html',{'otp': otp, 'username': username, 'password': password, 'email': email})
def reset(request):
    return render(request,'password reset.html')    

def review(request,product_id,slug):
    d=Product.objects.get(id=product_id)
    reviews = Review.objects.filter(post_id = product_id)
     
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data['review']
            c = reviews(post_id = product_id,review = review,user=request.user)
            c.save()

    else:
        form = ReviewForm()

    return render(request, 'review.html',{'d':d,'form': form,'reviews':reviews})       
def home(request):
    return render(request,'home.html')












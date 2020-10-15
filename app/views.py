from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import datetime
from app.models import Profile, Product, Comment
from app.forms import ProductForm, CommentForm

def index(request):
    products = Product.objects.all()

    return render(request, "app/index.html", {'products': products})

def about(request):
    return render(request, "app/about.html", {})

def blog_single(request, id):
    product = Product.objects.filter(id=id).first()
    comments = Comment.objects.filter(product_id=id)
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.user = request.user
            comment.product = product
            
            comment.save()
    else:
        commentForm = CommentForm()
    return render(request, "app/blog_single.html", {"product": product, 'commentForm': commentForm, 'comments': comments})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        if request.POST.get('password1') != request.POST.get('password2'):
            return HttpResponse('Password does not match!')
        password = request.POST.get('password1')
        
        # creating user
        User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
        )

        return redirect('signin')

    return render(request, "app/signup.html", {})    

def add_post(request):
    if request.method == 'POST':
        print("POST")
        productForm = ProductForm(request.POST, request.FILES)

        if productForm.is_valid():
            print("Valid")
            product = productForm.save(commit=False)
            product.save()
    else:
        print("GET")
        productForm = ProductForm()
    return render(request, "app/add_post.html", {'productForm': productForm})    
    
def user_profile(request):
    return render(request, "app/user_profile.html", {})   

    
def edit_user_profile(request):
    user = User.objects.get(id = request.user.id)
    user_profile = Profile.objects.filter(user=user).first()
    
    if request.method == 'POST':
        print("POST")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if username != '' and username != user.username:
            user.username = username
        if email != '' and email != user.email:
            user.email = email
        if password1 == password2 and password1 != "" and password2 != "":
            user.password = password1
        if gender and phone != "" and address != "":
            user_profile.phone=phone,
            user_profile.gender=gender,
            user_profile.address=address,
            print("PROFILE")
            print("AFTER")
            user_profile.save()
            print("SAVING PROFILE")

        
    context = {
        'username': user.username,
        'email': user.email,
    }
    if user_profile:
        context['gender'] = user_profile.gender
        context['phone'] = user_profile.phone
        context['address'] = user_profile.address
        context['birthday'] = user_profile.birthday
            

    return render(request, "app/edit_user_profile.html", context)   
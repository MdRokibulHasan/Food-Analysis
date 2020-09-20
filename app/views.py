from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "app/index.html", {})

def about(request):
    return render(request, "app/about.html", {})

def blog_single(request):
    return render(request, "app/blog_single.html", {})

def signin(request):
    return render(request, "app/signin.html", {})


def signup(request):
    return render(request, "app/signup.html", {})    

def add_post(request):
    return render(request, "app/add_post.html", {})    
    
def user_profile(request):
    return render(request, "app/user_profile.html", {})   

    
def edit_user_profile(request):
    return render(request, "app/edit_user_profile.html", {})   
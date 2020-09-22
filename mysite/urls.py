"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from app.views import (
    index,
    about,
    blog_single,
    signup,
    add_post,
    user_profile,
    edit_user_profile,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name="about"),
    path('blog_single/', blog_single, name="blog_single"),
    path('signup/', signup, name="signup"),  
    path('add_post/', add_post, name="add_post"),
    path('user_profile/', user_profile, name="user_profile"),
    path('edit_user_profile/', edit_user_profile, name="edit_user_profile"),
    path('signin/', auth_views.LoginView.as_view(template_name='app/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs, name='blogs'),
    path('blog-create/', blogs_create, name='blog_create'),
    path('blog-single/<int:pk>/', blog_single, name='blog_single'),
    path('blog-update/<int:pk>/', blog_update, name='blog_update'),
    path('services/', Services, name='services'),
    path('contact-us/', Contact, name='contact'),
    path('FAQ/', faq, name='faq'),

] 
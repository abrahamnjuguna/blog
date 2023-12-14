from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import * 
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def blogs(request):
    title = "Our Blogs"
    blogs = Blog.objects.all()
    recent_blogs = Blog.objects.order_by('date')[:6]
    context = {
        'title':title,
        'blogs':blogs,
        'recent_blogs':recent_blogs,
    }
    return render(request, 'home/blogs.html', context)


@login_required
def blogs_create(request):
    title = 'Blog Create'
    recent_blogs = Blog.objects.order_by('date')[:6]
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid:
            blog = form.save(commit=False)
            blog.save()
            return redirect('blogs')
        else:
            form = BlogForm(form.errors)
            context ={
                'form':form,
                'recent_blogs':recent_blogs,
                'title':'title'
            }
            return render(request,'home/blog-create.html',context)
    context = {
        'title':title,
        'form':form,
        'recent_blogs':recent_blogs,
    }
    return render(request, 'home/blogs_create.html', context)


def blog_single(request, pk):
    title = 'Single Blog'
    recent_blogs = Blog.objects.order_by('date')[:6]
    single_post = Blog.objects.get(id=pk)
    context = {
        'title':title,
        'single_post':single_post,
        'recent_blogs':recent_blogs,
    }
    return render(request, 'home/blog_single.html', context)


@login_required
def blog_update(request, pk):
    title = 'Blog Update'
    recent_blogs = Blog.objects.order_by('date')[:6]
    blog_obj = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog_obj)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog_obj)
        if form.is_valid():
            form.save()
            return redirect('blog_single', pk)
    context = {
        'title':title,
        'form':form,
        'recent_blogs':recent_blogs,
        'blog_obj':blog_obj,
    }
    return render(request, 'home/blog_update.html', context)

def Services(request):
    return render(request, 'home/services.html')


def Contact(request):
    title = 'Contact Us'
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        message_obj = Message.objects.create(
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            email = email,
            message = message
        )
        message_obj.save()
        messages.success(request,'Message Sent Successfully!')
        return redirect('contact')
    context = {
        'title':title,
    }
    return render(request, 'home/contact.html', context)


def faq(request):
    title = 'FAQ'
    recent_blogs = Blog.objects.order_by('date')[:6]
    context = {
        'title':title,
        'recent_blogs':recent_blogs,
    }
    return render(request, 'home/faq.html', context)

def about(request):
    return render(request, 'home/about.html')
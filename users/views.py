from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('home')

        else:
            return redirect('login')
            messages.error(request, 'Error wrong username/password')
    return render(request, 'users/log_in.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
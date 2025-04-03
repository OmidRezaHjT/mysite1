from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from accounts.forms import CustomUserCreationForm
def custom_login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        if not username_or_email or not password:
            return render(request, 'accounts/login.html', {'error': 'Username/email and password are required.'})

        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username_or_email = user.username
            except User.DoesNotExist:
                user = None
                return render(request, 'accounts/login.html', {'error': 'No user with that email found.'})

        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username/email or password.'})

    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')  
    
    form = CustomUserCreationForm(request.POST or None) 
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user) 
        return redirect('/')
    
    return render(request, 'accounts/signup.html', {'form': form})
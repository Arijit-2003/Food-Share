
# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically logs in the user after signup
            return redirect('home')  # We'll define the home view soon
    else:
        form = SignupForm()
    return render(request, 'userauth/signup.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm  # make sure this exists


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Redirect based on role
                if user.role == 'restaurant':
                    return redirect('/restaurant/dashboard/')
                elif user.role == 'ngo':
                    return redirect('/ngo/dashboard/')
                else:
                    return redirect('/user/dashboard/')

            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'userauth/signin.html', {'form': form})





from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')



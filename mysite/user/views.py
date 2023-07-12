from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print('Yay')
            return redirect('/calendar/make_appointment')
        else:
            messages.error(request, ('Error logging in!'))
            print('No')
            return redirect('/user/login')     
    else:
        # Return an 'invalid login' error message.
        return render(request, 'login1.html', {})
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!'))
            return redirect('/calendar/make_appointment')
        
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def logout1(request):
    logout(request)
    messages.success(request, ('You have been successfully logged out!'))
    return redirect('/user/login')
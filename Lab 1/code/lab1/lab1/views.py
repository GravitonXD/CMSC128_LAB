from django.shortcuts import redirect, render
from templates.createUser import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# render index.html when at /home
@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

# render login.html when at /login
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')

    return render(request, 'login.html', context={})

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

# render about.html when at /about
@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

# render contact.html when at /contact
@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

# render planner.html when at /planner
@login_required(login_url='login')
def planner(request):
    return render(request, 'planner.html')

# render profile.html when at /profile
@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
            else:
                messages.error(request, form.errors)
                return redirect('signup')

    return render(request, 'sign_up.html', context={'form': form})
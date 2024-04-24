from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Users

def login_user(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            print('user found')
            return redirect('redirect_users')
        else:
            # Handle invalid login (e.g., display an error message)
            print('user not found')
            return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password'})
   
    return render(request, 'accounts/login.html')

@login_required
def redirect_users(request):
    user = request.user
    if user.role == Users.STORE_KEEPER:
        return redirect('stock_dash') 
    elif user.role == Users.DEAN_OF_STUDY:
        return redirect('student_admin') 
    else:
        # Handle default redirection (e.g., redirect to a generic dashboard)
        return redirect('student_dashboard')  # Replace 'generic_dashboard' with the appropriate URL name for the generic dashboard

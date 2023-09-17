import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import PasswordCheckForm
from .models import PasswordCheck
from .tasks import analyze_password_strength

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = AuthenticationForm(request)  # Use AuthenticationForm here
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    # Retrieve the password checks for the logged-in user
    password_checks = PasswordCheck.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'myprojj/user_dashboard.html', {'password_checks': password_checks})

@login_required
def password_check(request):
    if request.method == 'POST':
        form = PasswordCheckForm(request.POST)
        if form.is_valid():
            # Get the password from the form
            password = form.cleaned_data.get('password')
            
            # Queue the password analysis task using Celery
            analyze_password_strength.delay(password, request.user.id)
            
            # Redirect to password check history page
            return redirect('password_check_history')
    else:
        form = PasswordCheckForm()
    return render(request, 'myprojj/password_check.html', {'form': form})

@login_required
def password_check_result(request, password_check_id):
    password_check = PasswordCheck.objects.get(id=password_check_id)
    return render(request, 'myprojj/password_check_result.html', {'password_check': password_check})

@login_required
def password_check_history(request):
    password_checks = PasswordCheck.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'myprojj/password_check_history.html', {'password_checks': password_checks})

@login_required
def password_check_delete(request, password_check_id):
    password_check = PasswordCheck.objects.get(id=password_check_id)
    password_check.delete()
    return redirect('myprojj/password_check_history')

# password check update view
@login_required
def password_check_update(request, password_check_id):
    password_check = PasswordCheck.objects.get(id=password_check_id)
    if request.method == 'POST':
        form = PasswordCheckForm(request.POST)
        if form.is_valid():
            # get the password from form
            password = form.cleaned_data.get('password')
            # calculate the strength score
            strength_score = 0
            # check if password contains uppercase
            if any(x.isupper() for x in password):
                strength_score += 1
            # check if password contains lowercase
            if any(x.islower() for x in password):
                strength_score += 1
            # check if password contains number
            if any(x.isdigit() for x in password):
                strength_score += 1
            # check if password contains special characters
            special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
            if any(x for x in password if re.match(special_characters, x)):
                strength_score += 1
            # check if password contains more than 8 characters
            if len(password) > 8:
                strength_score += 1
            # update the password check in db
            password_check.password = password
            password_check.strength_score = strength_score
            password_check.save()
            # redirect to password check result page
            return redirect('myprojj/password_check_result', password_check_id=password_check.id)
    else:
        form = PasswordCheckForm()
    return render(request, 'myprojj/assword_check_update.html', {'form': form, 'password_check': password_check})

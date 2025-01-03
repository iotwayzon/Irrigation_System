from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

def RegisterView(request):
    if request.method == 'POST':
       # getting user inputs from frontend
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')

       user_data_has_error = False
       if User.objects.filter(username=username).exists():
              user_data_has_error = True
              messages.error(request, 'Username already exists')

       if User.objects.filter(email=email).exists():
              user_data_has_error = True
              messages.error(request, 'Email already exists')
       # make aure password is at least 5 characters long
       if len(password) < 5:
              user_data_has_error = True
              messages.error(request, 'Password must be at least 5 characters')
       
       if not user_data_has_error:
              new_user = User.objects.create_user(
                     first_name = first_name,
                     last_name = last_name,
                     email = email,
                     username = username,
                     password = password
              )
              messages.success(request, 'Account created. Login now')
              return redirect('login')
       else:
              return redirect('register')

    return render(request, 'register.html')

def LoginView(request):
    if request.method == 'POST':
       # getting user inputs from frontend
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request=request, username=username, password=password)
       if user is not None:
              # login user if login credentials are correct
              login(request, user)
              # ewdirect to home page
              return redirect('home')
       else:
              # redirect back to the login page if credentials are wrong
              messages.error(request, 'Invalid username or password')
              return redirect('login')
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    
    return redirect('login')

def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Create a new reset id
            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()
            # Create password reset URL
            password_reset_url = request.build_absolute_uri(
                reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})
            )
            # Email content
            email_body = f"Reset your password using the link below:\n\n{password_reset_url}"

            email_message = EmailMessage(
                'Reset your password',  # Email subject
                email_body,            # Email body
                settings.EMAIL_HOST_USER,  # Email sender
                [email]                # Email receiver
            )
            email_message.fail_silently = True
            email_message.send()
            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")
            return redirect('forgot-password')

    return render(request, 'forgot_password.html')


def PasswordResetSent(request, reset_id):
     if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
     else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

def ResetPassword(request, reset_id):
    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            passwords_have_error = False

            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')

            if len(password) < 5:
                passwords_have_error = True
                messages.error(request, 'Password must be at least 5 characters long')

            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'Reset link has expired')

                password_reset_id.delete()

            if not passwords_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()

                messages.success(request, 'Password reset. Proceed to login')
                return redirect('login')
            else:
                # redirect back to password reset page and display errors
                return redirect('reset-password', reset_id=reset_id)

    except PasswordReset.DoesNotExist:
        
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

    return render(request, 'reset_password.html')



@login_required(login_url="/login")
def Home(request):
    return render(request, 'new_dashboard.html')

from django.utils.translation import gettext as _



from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer
from .forms import FarmerForm

@login_required(login_url="/login")
@permission_required("agri_app.view_farmer", login_url="/login", raise_exception=True)
def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'farmer/farmer_list.html', {'farmers': farmers})

@permission_required("agri_app.add_farmer", login_url="/login", raise_exception=True)
def farmer_create(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerForm()
    return render(request, 'farmer/farmer_form.html', {'form': form})

@permission_required("agri_app.change_farmer", login_url="/login", raise_exception=True)
def farmer_update(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerForm(instance=farmer)
    return render(request, 'farmer/farmer_form.html', {'form': form})

@permission_required("agri_app.delete_farmer", login_url="/login", raise_exception=True)
def farmer_delete(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        farmer.delete()
        return redirect('farmer_list')
    return render(request, 'farmer/farmer_confirm_delete.html', {'farmer': farmer})
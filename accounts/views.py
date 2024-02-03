from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, logout, authenticate, login as auth_login
from django.contrib import messages
import re


User = get_user_model()

# Create your views here.


# def signup_view(request):
#     if request.method == 'POST':
#         account = request.POST['account_type']
#         name = request.POST['name']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#         phone = request.POST['phone_num']
#         gender = request.POST['gender']

#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists. Please choose a different email.')
#             return redirect('signup_auth')

#         if pass1 != pass2:
#             messages.error(request, "Password and Confirm Password didn't match")
#             return redirect('signup_auth')

#         if account == '1':
#             if not all([name, email, pass1, pass2, gender, phone]):
#                 messages.error(request, 'All fields are required.')
#                 return render(request, 'accounts/signup.html')
            
#         if account == '2':
#             phone = None
#             if not all([name, email, pass1, pass2]):
#                 messages.error(request, 'All fields are required.')
#                 return render(request, 'accounts/signup.html')

#     #     my_user= User.objects.create_user(email=email, password = pass1)
#     #     my_user.name = name
#     #     my_user.phone_num = phone
#     #     my_user.gender = gender
#     #     my_user.account = account
#     #     my_user.save()

#     #     print(account, name, email)

#     #     messages.success(request, 'Account has been created successfully please login!')
#     #     return redirect('login_auth')
#     # return render(request, 'accounts/signup.html')

#         try:
#             my_user = User.objects.create_user(email=email, password=pass1)
#             my_user.name = name
#             my_user.phone_num = phone
#             my_user.gender = gender
#             my_user.account = account
#             my_user.save()
#             messages.success(request, 'Account has been created successfully. Please login!')
#             return redirect('login_auth')
#         except Exception as e:
#             messages.error(request, f'Error creating account: {e}')
#             return render(request, 'accounts/signup.html')

#     return render(request, 'accounts/signup.html')


def signup_view(request):
    if request.method == 'POST':
        account = request.POST['account_type']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phone = request.POST['phone_num']
        gender = request.POST['gender']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please choose a different email.')
            return redirect('signup_auth')

        if pass1 != pass2:
            messages.error(request, "Password and Confirm Password didn't match")
            return redirect('signup_auth')

        # Password validation
        if len(pass1) < 8:
            messages.error(request, 'Password should be at least 8 characters long.')
            return render(request, 'accounts/signup.html')
        if not re.search(r'\d', pass1) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', pass1):
            messages.error(request, 'Password should contain at least one number and one special character.')
            return render(request, 'accounts/signup.html')

        if account == '1':
            if not all([name, email, pass1, pass2, gender, phone]):
                messages.error(request, 'All fields are required.')
                return render(request, 'accounts/signup.html')
            
        if account == '2':
            phone = None
            if not all([name, email, pass1, pass2]):
                messages.error(request, 'All fields are required.')
                return render(request, 'accounts/signup.html')

        try:
            my_user = User.objects.create_user(email=email, password=pass1)
            my_user.name = name
            my_user.phone_num = phone
            my_user.gender = gender
            my_user.account = account
            my_user.save()
            messages.success(request, 'Account has been created successfully. Please login!')
            return redirect('login_auth')
        except Exception as e:
            messages.error(request, f'Error creating account: {e}')
            return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials!')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect ('/')
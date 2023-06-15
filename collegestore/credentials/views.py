from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def order(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        date = request.POST.get('date')
        age = request.POST.get('age')
        gender = request.POST.get('male')
        mobilno = request.POST.get('mobilno')
        email = request.POST.get('email')
        address = request.POST.get('address')
        main_category = request.POST.get('main_category')
        sub_category = request.POST.get('sub_category')

        # Check if all fields are filled
        if username and date and age and gender and mobilno and email and address and main_category and sub_category:
            # All fields are filled, display success message
            messages.success(request, 'Order Confirmed!')
        else:
            # One or more fields are missing, display error message
            messages.error(request, 'Please fill in all fields.')

        return render(request,'order.html')

    return render(request, 'order.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'orderr.html')
        else:
            messages.info(request, "INVALID CREDENTIALS")
            return render(request, 'login.html')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

        else:
            messages.info(request, "Password not matching")
            return render(request, 'register.html')
        return render(request, 'login.html')

    return render(request, "register.html")

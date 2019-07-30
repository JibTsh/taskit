from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
)
User = get_user_model()
# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("confirm_password")
        # Are all the fields complete
        if username and email and password and c_password:
            pass
        else:
            context = {
                "error": "You must fill in all the fields!"
            }
            return render(request, "accounts/register.html", context)
        # Is the username and email unique
        try:
            user = User.objects.get(username=username)
            if user is not None:
                context = {
                "error": "The Username or Email already exists!"
                }
                return render(request, "accounts/register.html", context)
            User.objects.get(email=email)
            context = {
            "error": "The Username or Email already exists!"
            }
            return render(request, "accounts/register.html", context)
        except User.DoesNotExist:
            pass

        #Check if passwords are the same
        if password != c_password:
            context = {
                "error": "The Passwords don't match!"
            }
            return render(request, "accounts/register.html", context)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('/')

    return render(request, "accounts/register.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Are all the fields complete
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        context = {
            "error": "Wrong User Information!"
            }
        return render(request, "accounts/login.html", context)
    return render(request, "accounts/login.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
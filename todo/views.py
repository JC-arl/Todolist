from django.shortcuts import render

# Create your views here.
def login_main(request):
    return render(request, 'login.html',{})

def login_signin(request):
    return render(request, 'login_signin.html',{})

def login_signup(request):
    return render(request, 'login_signup.html',{})
def main_page(request):
    return render(request, 'main_page.html',{})

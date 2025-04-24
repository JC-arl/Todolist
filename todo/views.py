from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def login_main(request):
    return render(request, 'login.html',{})

def login_signin(request):
    return render(request, 'login_signin.html',{})

def login_signup(request):
    return render(request, 'login_signup.html',{})


@login_required    #로그인 확인된 사용자만 main_page 접근 가능
def main_page(request):
    return render(request, 'main_page.html',{})

def login(request):
    respons_data = {}
    if request.method == 'POST':
        login_id = request.POST.get('id_input','')
        login_pwd = request.POST.get('pwd_input','')
        user = authenticate(request, username=login_id, password=login_pwd)
        if user is not None:
            login(request, user) # 세션에 사용자 등록
            return redirect('main_page')
        else:
            messages.error(request, '아이디 또는 비밀번호가 일치하지 않습니다.')
            return redirect('login_signin')
    return render(request, 'login_signin.html',{})
   
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('id_input','')
        passowrd = request.POST.get('pwd_input','')
        pwd_checked = request.POST.get('pwdcheck_input','')
        if passowrd != pwd_checked:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('login_signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 사용중인 아이디입니다.')
            return redirect('login_signup')
        
        User.objects.create_user(username=username, password=passowrd)
        messages.success(request, '회원가입이 완료되었습니다.')
        return redirect('login_signin')
    return render(request, 'login_signup.html',{})

def logout(request):
    logout(request)
    return redirect('login_main')

        


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def login_main(request):
    if request.method == 'POST':
        user_id = request.POST.get('id_input')
        password = request.POST.get('pwd_input')
        password_check = request.POST.get('pwdcheck_input')
        
        if password != password_check:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('login_signup')
            
        try:
            user = User.objects.create_user(
                username=user_id,
                password=password
            )
            return redirect('login')  # 로그인 페이지로 리다이렉트
        except Exception as e:
            messages.error(request, '회원가입 중 오류가 발생했습니다.')
            return redirect('login_signup')
            
    return render(request, 'login_signup.html') 
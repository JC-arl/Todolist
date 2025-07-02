from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm

# Create your views here.
def login_main(request):
    return render(request, 'login.html',{})

def login_signin(request):
    return render(request, 'login_signin.html',{})

def login_signup(request):
    return render(request, 'login_signup.html',{})


@login_required
def main_page(request):
    user = request.user
    todos = Todo.objects.filter(user=user, is_done=False)
    done_todos = Todo.objects.filter(user=user, is_done=True)
    undone_todos = Todo.objects.filter(user=user, is_done=False)
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # ← 여기서 'due_date' 값 확인 가능
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('main_page')

    return render(request, 'main_page.html', {
        'todos': todos,
        'form': form,
        'done_todos': done_todos,
        'undone_todos': undone_todos
        })

def UserLogin(request):
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

def user_logout(request):
    logout(request)
    return redirect('login_main')

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user, is_done=False) # 로그인한 사용자의 할 일 목록 조회
    form = TodoForm()            # 폼 초기화
    
    if request.method == 'POST':            # POST 요청이 있을 경우
        form = TodoForm(request.POST)      # 폼 데이터 저장
        if form.is_valid():               # 폼 데이터 유효성 검사
            print(form.cleaned_data)
            todo = form.save(commit=False) # 데이터베이스에 저장하지 않고 메모리에 저장
            todo.user = request.user       # 로그인한 사용자 연결
            todo.save()                    # 데이터베이스에 저장
            return redirect('todo_list')   # 목록 페이지로 리다이렉트
    return render(request, 'main_page.html', {'todos':todos, 'form':form}) # 목록 페이지 렌더링

from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model  #사용자가 데이터베이스 안에 있는지 검사
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up_view(request):
    if request.method=='GET':
        user=request.user.is_authenticated  #user존재여부
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign-up.html')

    elif request.method=='POST':
        username = request.POST.get('username', '')
        password=request.POST.get('password','')
        password2=request.POST.get('password2','')
        nickname=request.POST.get('nickname','')


        if password!=password2:
            #패스워드가 같지 않다고 알람
            return render(request,'user/sign-up.html',{'error':'패스워드를 확인해주세요'})
        else:
            if nickname=='' or password=='':
                return render(request, 'user/sign-up.html', {'error': '사용자 닉네임과 비밀번호는 필수값 입니다'})
            exist_user=get_user_model().objects.filter(username=username) #닉네임중복확인하기 위해
            if exist_user: #중복된 닉네임이 있다면 다시 입력
                return render(request, 'user/sign-up.html',{'error':'사용자가 존재합니다'})
            else: #중복되지 않는다면 User db에 저장
                User.objects.create_user(username=username,password=password,nickname=nickname)
                return redirect('/sign-in')



def sign_in_view(request):
    return render(request, 'user/sign-in.html')


def preference_view(request):
    return render(request, 'user/preference.html')

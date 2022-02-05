from django.shortcuts import render, redirect
from .models import User, UserProfile
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # user존재여부
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign-up.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')  # username을 이메일형식으로 가져옴
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        nickname = request.POST.get('nickname', '')  # 로그인할시 사용할 nickname

        if password != password2:
            # 패스워드가 같지 않다고 알람
            return render(request, 'user/sign-up.html', {'error': '패스워드를 확인해주세요'})
        else:
            # 이미 html에서 requried를 통해 해줌
            # if nickname=='' or password=='': #닉네임과 password 필수입력
            #     return render(request, 'user/sign-up.html', {'error': '사용자 닉네임과 비밀번호는 필수값 입니다'})
            exist_user = get_user_model().objects.filter(username=username)  # 같은 이메일은 사용불가
            if exist_user:  # 중복된 이메일일경우
                return render(request, 'user/sign-up.html', {'error': '사용자가 존재합니다'})
            else:  # 중복되지 않는 이메일일 경우 db에 저장
                User.objects.create_user(username=username, password=password, nickname=nickname)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')

        me = auth.authenticate(request, username=username, password=password)  # username과 password가 같은 사용자를 찾아라
        print(me)  # me(사용자가 있다면 저장된 사용자의 정보가져옴/없다면 None)

        if me is not None:  # 사용자가 있다면 로그인
            auth.login(request, me)

            # /prefer로 이동여부
            user = request.user
            print("유저정보 가져오기:", user)

            profile = UserProfile.objects.filter(user=user)
            print("선호조사 정보존재여부:", profile)

            if profile:  # user_id값이 user_profile에 있다면 prefer건너뛰기
                return redirect('/')
            else:  # user_id값이 user_profile에 없다면 prefer로 이동
                return redirect('/prefer')
        else:  # 사용자가 없다면(None) 다시 로그인창 띄우기
            return render(request, 'user/sign-in.html', {'error': '사용자 이름 혹은 패스워드를 확인해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:  # 로그인되면 prefer부분이 아니라 base로 간다
            return redirect('/')
        else:
            return render(request, 'user/sign-in.html')


@login_required
def preference_view(request):
    if request.method == "GET":
        return render(request, 'user/preference.html')
    elif request.method == "POST":
        body = request.POST.get('chk1')
        tannin = request.POST.get('chk2')
        acidity = request.POST.get('chk3')
        sweetness = request.POST.get('chk4')
        user = request.user
        # UserProfile에 저장
        my_prefer = UserProfile()
        my_prefer.user = user
        my_prefer.body = body
        my_prefer.tannin = tannin
        my_prefer.acidity = acidity
        my_prefer.sweetness = sweetness
        my_prefer.save()

        return redirect('/')


@login_required()
def logout(request):
    auth.logout(request)  # request에 값이 있는지session에서 알아서 찾아내준다.
    return redirect("/sign-in")

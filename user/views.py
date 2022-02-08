import pandas
from django.shortcuts import render, redirect
from .models import User, UserProfile
from recommendation.models import WineRecommend ,Wine
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


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
            if nickname == '' or password == '':  # 닉네임과 password 필수입력
                return render(request, 'user/sign-up.html', {'error': '사용자 닉네임과 비밀번호는 필수값 입니다'})
            exist_user = get_user_model().objects.filter(username=username)  # 같은 이메일은 사용불가
            if exist_user:  # 중복된 이메일일경우
                return render(request, 'user/sign-up.html', {'error': '사용자가 존재합니다'})
            else:  # 중복되지 않는 이메일일 경우 db에 저장
                User.objects.create_user(username=username, password=password, nickname=nickname)
                me = auth.authenticate(request, username=username, password=password)
                auth.login(request, me)
                return redirect('/prefer')


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')

        me = auth.authenticate(request, username=username, password=password)  # username과 password가 같은 사용자를 찾기 없으면 None

        if me is not None:  # 사용자가 있다면 로그인
            auth.login(request, me)

            # /prefer로 이동여부 (=profile = UserProfile.objects.filter(user=request.user))
            if me.surveyed:  # prefer survey를 완료했다면 추천 와인으로
                return redirect('/')
            else:  # survey를 완료하지 않았다면 /prefer로 이동
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
        # 사용자 선호조사 user_profile에 저장

        body = request.POST.get('chk1')
        tannin = request.POST.get('chk2')
        acidity = request.POST.get('chk3')
        sweetness = request.POST.get('chk4')
        user = request.user

        my_prefer = UserProfile()  # UserProfile에 저장
        my_prefer.user = user
        my_prefer.body = body
        my_prefer.tannin = tannin
        my_prefer.acidity = acidity
        my_prefer.sweetness = sweetness
        my_prefer.save()

        user.surveyed = True  # Preference survey 완료
        user.save()

        # 추천하는 와인 user_recommend에 저장

        df = pd.read_csv("Wine.csv")
        df = df.drop(
            columns=['Name', 'Link', 'Country', 'Type', 'Flavor', 'Comment', 'Region', 'Index', 'Rating', 'Img'],
            axis=1)  # 문자열빼고
        df = df.astype(np.float32)  # 32비트로 바꿔줘야 keras에서 알아듣는다.
        x = np.array([body, tannin, acidity, sweetness])
        userdf_1 = np.tile(x, (100, 1))  # 100*4컬럼으로 만들어줌
        print(userdf_1)
        userdf = userdf_1.astype(np.float32)
        wine_based_collab = cosine_similarity(df, userdf)  # 유저의 프리퍼런스 행을 수치화한 자료가 들어가서
        wine_based_collab = pd.DataFrame(
            wine_based_collab)
        result = (wine_based_collab[0].sort_values(ascending=False)[:8])
        print(result)
        list = result.index.tolist()  # 상위 8개 인덱스만 가져오기
        for wineid in list:
            print(wineid)
            wine = Wine.objects.get(id=wineid + 1)
            print(wine)
            new_recommend = WineRecommend()
            new_recommend.user = user
            new_recommend.wine = wine
            new_recommend.save()

        return redirect('/')


@login_required()
def logout(request):
    auth.logout(request)  # request에 값이 있는지session에서 알아서 찾아내준다.
    return redirect("/sign-in")


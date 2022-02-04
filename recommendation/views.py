from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from recommendation.models import Wine


def home(request):
    user = request.user.is_authenticated
    print(user)
    if user:  # 사용자가 있으면 main으로
        return redirect('/main')
    else:  # 사용자가 없으면 로그인화면으로
        return redirect('/sign-in')


def main(request):
    wines = Wine.objects.filter(region='Napa Valley')  # 일단은 유저 추천 대신 필터로 적용해둠
    return render(request, 'recommendation/recommend.html', {'wines': wines})


@login_required()
def detail(request):
    if request.method == "GET":
        return render(request, "recommendation/wine_information.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from recommendation.models import Wine


def home(request):
    user = request.user.is_authenticated
    print(user)
    if user:  # 사용자가 있으면 main으로
        return redirect('/wine_recommend')
    else:  # 사용자가 없으면 로그인화면으로
        return redirect('/sign-in')


@login_required
def wine_recommend(request):
    wines = Wine.objects.filter(region='Napa Valley')  # 일단은 유저 추천 대신 필터로 적용해둠
    return render(request, 'recommendation/wine_recommend.html', {'wines': wines})


@login_required
def wine_all(request):
    wines = Wine.objects.all()
    if request.method == "GET":
        return render(request, "recommendation/wine_all.html", {'wines': wines})


@login_required
def wine_detail(request, id):
    if request.method == "GET":
        return render(request, "recommendation/wine_detail.html")


@login_required
def my_pic(request):
    if request.method == "GET":
        return render(request, "recommendation/my_pic.html")

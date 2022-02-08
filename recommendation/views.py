from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recommendation.models import Wine, WineRecommend, WineProfile
from user.models import User


def home(request):
    user = request.user.is_authenticated
    print('user is authenticated:', user)
    if user:  # 사용자가 있으면 main으로
        return redirect('/wine-recommend')
    else:  # 사용자가 없으면 로그인화면으로
        return redirect('/sign-in')


@login_required
def wine_recommend(request):
    me = request.user
    if me.surveyed:
        recommend_wine = WineRecommend.objects.filter(user=me)
        print(recommend_wine)
        my_list = []
        for wine in recommend_wine:
            my_list.append(wine.wine_id)
        print(my_list)
        wines = Wine.objects.all()
        return render(request, 'recommendation/wine_recommend.html', {'list': my_list, 'wines': wines})
    else:
        return redirect('/prefer')


@login_required
def wine_all(request):
    wines = Wine.objects.all()  # wines 전체
    if request.method == "GET":
        return render(request, "recommendation/wine_all.html", {'wines': wines})


@login_required
def wine_detail(request, id):
    wine = Wine.objects.get(id=id)  # wine id로 선별
    wine_profile = WineProfile.objects.get(wine=wine)
    wine_id = wine.yturl[-11:]
    print(wine_id)
    if request.method == "GET":
        return render(request, "recommendation/wine_detail.html",
                      {'wine': wine, 'wine_profile': wine_profile, 'wine_id': wine_id})


# my pick 페이지
@login_required
def my_pick(request):
    if request.method == "GET":
        picks = Wine.objects.filter(mypic=request.user)  # 와인 class의 mypic M:M 필드 통해서 데이터 찾기
        wine_list = [pick for pick in picks]  # QuerySet 내의 와인 오브젝트 리스트 형태로 반환
        return render(request, "recommendation/my_pick.html", {'wines': wine_list})


# 와인 mypick 저장 기능
def wine_save_toggle(request, wine_id):
    wine = get_object_or_404(Wine, id=wine_id)
    me = get_object_or_404(User, id=request.user.id)

    check_saved_wine = me.my_pic.filter(id=wine_id)

    if check_saved_wine.exists():
        me.my_pic.remove(wine)
        wine.saved_count -= 1
        wine.save()
    else:
        me.my_pic.add(wine)
        wine.saved_count += 1
        wine.save()

    return redirect('recommendation:wine-recommend')


# 검색 기능
def search(request):
    query = None
    products = None

    if 'search_word' in request.GET:
        query = request.GET.get('search_word')
        products = Wine.objects.all().filter(
            Q(name__contains=query) | Q(type__contains=query) | Q(region__icontains=query) | Q(
                country__icontains=query) | Q(primary_flavors__icontains=query)).distinct()
        print('products', products)
    return render(request, 'recommendation/search_result.html', {'query': query, 'wines': products})

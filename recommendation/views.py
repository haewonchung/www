from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recommendation.models import Wine
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
        wines = Wine.objects.filter(region='Napa Valley')
        return render(request, 'recommendation/wine_recommend.html', {'wines': wines})
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
    if request.method == "GET":
        return render(request, "recommendation/wine_detail.html", {'wine': wine})


@login_required
def my_pic(request, id):
    my_wine = Wine.objects.get(id=id)  # 추후 변경 예정
    if request.method == "GET":
        return render(request, "recommendation/my_pick.html", {'wine': my_wine})


def wine_save_toggle(request, wine_id):
    wine = get_object_or_404(Wine, id=wine_id)
    # user = request.user
    # me = User.objects.get(user=user)
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


# 검색 기능 구현
# def search(request):
#     # search_list = Wine.objects.filter(name__icontains="Cabernet")
#     # search_word = request.GET['search-word']
#     if request.method == "GET":
#         # search_word = request.GET.get('search', '')
#         search_word = request.GET['search_word']
#         if search_word:
#             search_list = Wine.objects.filter(
#                 Q(name__icontains=search_word) | Q(type__icontains=search_word) |
#                 Q(region__icontains=search_word) | Q(country__icontains=search_word) |
#                 Q(primary_flavors__icontains=search_word))  # 중복제거
#             print('search_list', search_list)
#             return render(request, 'recommendation/search_result.html', {'search_word': search_word, 'wines': search_list})
#         else:
#             return render(request, 'recommendation/search_result.html')


def search(request):
    query = None
    products = None

    if 'search_word' in request.GET:
        query = request.GET.get('search_word')
        products = Wine.objects.all().filter(Q(name__contains=query) | Q(type__contains=query) | Q(region__icontains=query) | Q(country__icontains=query)|Q(primary_flavors__icontains=query)).distinct()
        print('products', products)
    return render(request, 'recommendation/search_result.html', {'query': query, 'wines': products})


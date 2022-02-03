from django.shortcuts import render,redirect
# from .models import
from django.contrib.auth.decorators import login_required

def home(request):
    user=request.user.is_authenticated
    print(user)
    if user:  #사용자가 있으면 main으로
        return redirect('/main')
    else:  #사용자가 없으면 로그인화면으로
        return redirect('/sign-in')

def main(request):
    return render(request,'recommendation/recommend.html')



# def wineinfo(request,id):
    # return render(request,'wine_infromation/wine_information.html')
from django.shortcuts import render


# Create your views here.
def sign_up_view(request):
    return render(request, 'user/sign-up.html')


def sign_in_view(request):
    return render(request, 'user/sign-in.html')


def preference_view(request):
    return render(request, 'user/preference.html')

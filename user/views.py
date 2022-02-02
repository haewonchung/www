from django.shortcuts import render


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/sign-up.html')
    elif request.method == 'POST':  # POST 메서드로 요청이 들어 올 경우

        return ""


def sign_in_view(request):
    return render(request, 'user/sign-in.html')


def preference_view(request):
    return render(request, 'user/preference.html')

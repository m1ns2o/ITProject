from django.shortcuts import render
from sruser.models import Sruser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        print(re_password)
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            sruser = Sruser(
                username=username,
                useremail=useremail,
                password=make_password(password) 
            )

            sruser.save()

        return render(request, 'register.html', res_data)
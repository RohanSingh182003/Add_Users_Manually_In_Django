from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# user - admin
# password - admin
def index(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        params = {'reject':'You are already an user...'}
        if User.objects.filter(username=user_name).exists(): #Check if the user is already exist or not
            return render(request,'index.html',params)
        params2 = {'success':'Congratulations! You are an User now..'}
        user = User.objects.create_user(user_name)
        user.set_password(user_password)
        user.save()
        return render(request,'index.html',params2)

    return render(request,'index.html')

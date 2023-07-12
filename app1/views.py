from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return HttpResponse("User has been create successfuly")
            return redirect('login')

    return render(request,'signup.html')

def Loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!")
    return render(request,'signin.html')
    
def Logout(request):
    logout(request)
    return redirect('login')

# def ForgotPass(request):

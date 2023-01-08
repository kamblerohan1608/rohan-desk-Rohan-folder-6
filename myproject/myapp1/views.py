from django.shortcuts import render,redirect
from .models import UserInfo

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        qualification = request.POST['qualification']
        contact = request.POST['contact']
        email = request.POST['email']
        address = request.POST['address']

        info = UserInfo(fname=fname,lname=lname,qualification=qualification,contact=contact,email=email,address=address)

        info.save()

        return redirect('user_info')

    return render(request,'index.html')

def user_info(request):

    info=UserInfo.objects.all()

    data={"info":info}

    return render(request,'user_info.html',data)

from django.shortcuts import render
from .models import HomePageInfo

# Create your views here.

def home(request):
    homePageInfo = HomePageInfo.objects.all()
    return render(request,'myhome/home.html',{'homePageInfo':homePageInfo})



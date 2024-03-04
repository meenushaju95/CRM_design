from django.shortcuts import render


def home(request):
   
    return render(request,'land_page.html')



from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    content = {'now' : datetime.datetime.now()}
    return render(request, 'Home.html', locals())

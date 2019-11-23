from django.shortcuts import render
from django.http import HttpResponse
from .models import destination


def index(request):
    dest1 = destination()
    dest1.name  ='karachi'
    dest1.price =200 
    dest1.desc='the city that never sleep or city of light'
    dest1.special= True 
    dest1.img='destination_1.jpg'

    dest2 = destination()
    dest2.name='Lahore'
    dest2.price =300 
    dest2.desc='the city that never sleep or city of light'
    dest2.special=False
    dest2.img='destination_2.jpg'

    dest3 = destination()
    dest3.name='islamabad'
    dest3.price =400 
    dest3.desc='the city that never sleep or city of light'
    dest3.special=False
    dest3.img='destination_3.jpg'

    dests = [dest1 , dest2 , dest3]

    return render(request,'index.html',{'dests': dests})

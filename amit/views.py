from django.shortcuts import render
from .models import Variety

# Create your views here.
def amit(request):
    amits=Variety.objects.all()
    return render(request,'amit/amit.html',{'amits':amits})

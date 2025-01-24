from django.shortcuts import render
from .models import testModel
# Create your views here.

def test(request):
    chais = testModel.objects.all()
    return render(request,"myapp/myapp.html",{"chais":chais})

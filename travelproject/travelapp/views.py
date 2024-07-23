from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
# def addition(request):
#     x = int(request.GET['n1'])
#     y = int(request.GET['n2'])
#     res = x + y
#     return render(request, "abt.html",{'result':res})


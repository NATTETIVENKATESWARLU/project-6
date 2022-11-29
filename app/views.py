from django.shortcuts import render

# Create your views here.
def mass(request):
    return render(request,'mass.html')


def venkey(request):
    return render(request,'venkey.html')
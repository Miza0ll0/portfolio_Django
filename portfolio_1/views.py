from django.shortcuts import render


def index(request):
    index = render(request, "index.html")
    return index




def test(request):
    test = render(request,"test.html")
    return test


from .models import *

def portfolio_view(request):
    about = About.objects.first()
    projects = Project.objects.all()
    exp = Exp.objects.all()
    return render(request, 'test.html', {
        'about': about,
        'projects': projects,
        'exp': exp,
    })
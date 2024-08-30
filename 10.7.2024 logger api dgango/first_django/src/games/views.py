from django.shortcuts import render

# Home view 

def home(request):
    return render(request, "home.html", {"active" : "home"})


def about(request):
    return render(request, "about.html", {"active" : "about"})
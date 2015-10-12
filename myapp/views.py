from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
                "form": "(Home) Hello World!",
            }
    return render(request, "home.html", context)

def about(request):
    context = {
                "form": "(About) Hello World!",
            }
    return render(request, "about.html", context)

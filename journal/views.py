from django.shortcuts import render

def index(request):
    return render(request, 'journal/index.html')

# Create your views here.

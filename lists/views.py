from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html') # takes request and name of template to render
    

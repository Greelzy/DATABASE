from django.shortcuts import render


def home_page(request):
    return render(request, 'Home/home_page.html')

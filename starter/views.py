from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return render(request, "starter/landing_page.html")

def movie_list(request):
	return render(request, "starter/movie_list.html")

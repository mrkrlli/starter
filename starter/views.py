from django.shortcuts import render
from djang.http import HttpResponse

def landing_page(request):
    return render(request, "starter/landing_page.html")

def movie_list(request):
	return HttpResponse('movie list page')

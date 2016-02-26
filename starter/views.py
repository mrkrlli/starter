from django.shortcuts import render
from django.http import HttpResponse
import json

def landing_page(request):
    return render(request, "starter/landing_page.html")

def movie_list(request):
	#return all movies to the view
	json_data = open('starter/data/more_movies.json') 
	data1 = json.load(json_data)
	json_data.close()
	movie_list = data1['movies']
	context = {'movie_list': movie_list}

	return render(request, "starter/movie_list.html", context)

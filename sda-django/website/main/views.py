from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import  HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.

def startpage_reponse(request):
    #return HttpResponse("Witamy w aplikacji")
    return render(request, "start.html")

def infopage_response(request):
    return HttpResponse("<br/>".join(dir(request)))

def movielist_response(request):
    all_movies = Movie.objects.all().order_by('title')
    return render(request, "movie-list.html", { "movies" : all_movies })

def movieadd_response(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        #return redirect("movie_list") # OK
        return redirect(movielist_response)
    return render(request, "movie-add.html", {"form":form})

def movieedit_response(request, id):
    # old-scholl rozwiązanie
    #try:
    #    movie = Movie.objects.get(pk=id)
    #except:
    #    raise Http404("nie ma takiego filmu")
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        # return redirect("movie_list") # OK
        return redirect(movielist_response)
    return render(request, "movie-add.html", {"form": form, "edit":True})

def moviedel_response(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == "POST":
        movie.delete()
        return redirect(movielist_response)
    return render(request, "movie-del.html", { "movie":movie})
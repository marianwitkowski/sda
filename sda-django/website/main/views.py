from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import  HttpResponse, Http404
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def startpage_reponse(request):
    #return HttpResponse("Witamy w aplikacji")
    return render(request, "start.html")

def infopage_response(request):
    #return HttpResponse("<br/>".join(dir(request)))
    return HttpResponse(request.path)

def movielist_response(request):
    all_movies = Movie.objects.all().order_by('title')
    return render(request, "movie-list.html", { "movies" : all_movies })

@login_required()
def movieadd_response(request):
    # wstawka na potrzeby sprawdzania zalogowania usera
    #if not request.user.is_authenticated:
    #    return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        #return redirect("movie_list") # OK
        return redirect(movielist_response)
    return render(request, "movie-add.html", {"form":form})

@login_required()
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

@login_required()
def moviedel_response(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == "POST":
        movie.delete()
        return redirect(movielist_response)
    return render(request, "movie-del.html", { "movie":movie})

def moviedetails_response(request, id):
    movie_obj = get_object_or_404(Movie, pk=id)
    comments = Comment.objects.filter(movie=movie_obj)
    return render(request, "movie-details.html",
                  { "movie" : movie_obj, "comments": comments } )

def logout_done(request):
    return render(request, "logout-done.html")
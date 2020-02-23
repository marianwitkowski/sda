from django.urls import path
from .views import *

urlpatterns = [
    path("", startpage_reponse),
    path("info", infopage_response),
    path("list", movielist_response, name="movie_list"),
    path("movieadd", movieadd_response, name="movie_add"),
    path("movieedit/<int:id>", movieedit_response, name="movie_edit"),
    path("moviedel/<int:id>", moviedel_response, name="movie_del" )
]
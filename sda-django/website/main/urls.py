from django.urls import path
from .views import *

# import domyślnych widoków na potrzeby logowania
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path("", startpage_reponse),
    path("info", infopage_response),
    path("list", movielist_response, name="movie_list"),
    path("movieadd", movieadd_response, name="movie_add"),
    path("movieedit/<int:id>", movieedit_response, name="movie_edit"),
    path("moviedel/<int:id>", moviedel_response, name="movie_del" ),
    path("list/<int:id>", moviedetails_response, name="movie_details" ),

    # ścieżki do widoków logowania/wylogowania
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("logout-done", logout_done)
]
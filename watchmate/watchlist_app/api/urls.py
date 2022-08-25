from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import StreamPlatformAV, StreamPlatformDetailsAV, WatchListAV, WatchListDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="watch-list"),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name="movie-details"),
    
    path('stream/', StreamPlatformAV.as_view(), name="stream-platform"),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name="stream-details"),
]
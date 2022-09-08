from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import (ReviewDetail, StreamPlatformAV, StreamPlatformDetailsAV, 
                                     WatchListAV, WatchListDetailAV, ReviewList, ReviewCreate)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="watch-list"),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name="movie-details"),
    
    path('stream/', StreamPlatformAV.as_view(), name="stream-platform"),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name="streamplatform-detail"),
    
    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name="review-create"),
    path('stream/<int:pk>/review', ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),
]
from django.urls import path
from .views import *

urlpatterns = [
    
    path('list/',  WatchListAV.as_view(), name ='movie_list'),
    path('<int:pk>', WatchLDetailAV.as_view(), name ='movie_detail'),

    path('stream/', StreamPlatformAV.as_view(), name ='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name ='stream_detail'),

    path('stream/<int:pk>/review', StreamPlatformDetailAV.as_view(), name ='stream_detail'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name ='review_detail'),

    # path('review', ReviewList.as_view(), name ='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name ='review_detail'),



]


 
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('stream', StreamPlatformVS, basename ='streamplatform')



urlpatterns = [
    
    path('list/',  WatchListAV.as_view(), name ='movie_list'),
    path('<int:pk>', WatchLDetailAV.as_view(), name ='movie_detail'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name ='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name ='stream_detail'),

    path('stream/<int:pk>/review', ReviewList.as_view(), name ='stream-list'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name ='stream-create'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name ='review-detail'),

    # path('review', ReviewList.as_view(), name ='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name ='review_detail'),


] 


  
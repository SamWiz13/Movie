from core.models import WatchList, StreamPlatform, Review
from core.api.serializers import WatchListSerializer,StreamPlatformSerializer, ReviewSerializer

from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, mixins
from rest_framework.views import APIView


class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
   
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many = True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView): 
    
    def get(self, request,pk):
        try:
            platform =StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status =status.HTTP_404_NOT_FOUND)

        serializer =StreamPlatform(platform)
        return Response(serializer.data)  

    def put(self, request, pk):
        platform =WatchList.objects.get(pk=pk)
        serializer =StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        movie =StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        platform =WatchList.objects.all()
        serializer =WatchListSerializer(platform, many = True)
        return Response(serializer.data)
        

    def post(self, request):
        serializer =WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchLDetailAV(APIView): 
    
    def get(self, request,pk):
        try:
            movies =WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status =status.HTTP_404_NOT_FOUND)

        serializer =WatchListSerializer(movies)
        return Response(serializer.data)  

    def put(self, request, pk):
        movies =WatchList.objects.get(pk=pk)
        serializer =WatchListSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        movie =WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)






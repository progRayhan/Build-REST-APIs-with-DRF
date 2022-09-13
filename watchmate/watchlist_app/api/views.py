from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import (WatchListSerializer, StreamPlatformSerializer,
                                           ReviewSerializer)
# from rest_framework.decorators import api_view
# from rest_framework import mixins
from rest_framework import generics

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        # my method goes here
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
        
        serializer.save(watchlist=movie, review_user=review_user)
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        # serializer = StreamPlatformSerializer(platform, many=True)
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
                
class StreamPlatformDetailsAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'errors':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WatchListAV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        watch = WatchList.objects.all()
        serializer = WatchListSerializer(watch, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchListDetailAV(APIView):
    def get(self, request,pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'errors':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(watch)
        return Response(serializer.data)
        
    def put(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


    
    
# class MovieListAV(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)  
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# class MovieDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'errors':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):
    # if request.method == 'GET':
        # movies = Movie.objects.all()
        # serializer = MovieSerializer(movies, many=True)  
        # return Response(serializer.data)
    
#     if request.method == 'POST':
        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
        
        # try:
        #     movie = Movie.objects.get(pk=pk)
        # except Movie.DoesNotExist:
        #     return Response({'errors':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # serializer = MovieSerializer(movie)
        # return Response(serializer.data)
    
#     if request.method == 'PUT':
        # movie = Movie.objects.get(pk=pk)
        # serializer = MovieSerializer(movie, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
        # movie = Movie.objects.get(pk=pk)
        # movie.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        
        
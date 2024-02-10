from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from User.models import User
from User.serializers import UserSer
from .models import (News, Comment, Photo, Like, LikeComment)
from .serializers import (NewsSer, NewsGetSer,
                        PhotoSer, CommentSer,
                        CommentGetSer)


class AllList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        news = News.objects.all()
        comment = Comment.objects.all()
        photo = Photo.objects.all()
        user = User.objects.all()
        news_ser = NewsSer(news, many=True)
        comment_ser = CommentSer(comment, many=True)
        photo_ser = PhotoSer(photo, many=True)
        user_ser = UserSer(user, many=True)
        return Response((news_ser.data, comment_ser.data, photo_ser.data, user_ser.data))


class PhotoList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        photo = Photo.objects.all()
        ser = PhotoSer(photo, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = PhotoSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class NewsList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        news = News.objects.all()
        ser = NewsGetSer(news, many=True)
        return Response(ser.data)
    
    def post(self, request):
        photo_list = request.data.getlist('photo', [])
        ser = NewsSer(data=request.data)
        if ser.is_valid():
            news = ser.save()
            for x in photo_list:
                photo = Photo.objects.get(photo=x)
                news.photo.add(photo)
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class NewsDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        news = News.objects.get(id=id)
        news.viewed_list = news.viewed_list+0
        news.sum_of_vieved_list()
        ser = NewsSer(news)
        if Comment.objects.get(news=news):
            comment = Comment.objects.get(news=news)
            commentser = NewsGetSer(comment, many=True)
            return Response((ser.data, commentser.data))
        return Response(ser.data)
    
    def post(self, request, id):
        news = News.objects.get(id=id)
        ser = CommentSer(request.data)
        if ser.is_valid():
            comment = ser.validated_data['comment']
            Comment.objects.create(
                comment=comment,
                user=request.user,
                news=news
                )
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)

    def patch(self, request, id):
        news = News.objects.get(id=id)
        ser = NewsSer(data=request.data, instance=news, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        news = News.objects.get(id=id)
        news.delete()
        return Response({'message': 'Deleted successfully'})


# class CommentList(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         news = News.objects.get()
#         comment = Comment.objects.get(id=id)
#         ser = CommentGetSer(comment)
#         return Response(ser.data)
    
#     def post(self, request):
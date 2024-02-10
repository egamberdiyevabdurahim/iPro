from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import User
from News.models import Like, News, Comment, LikeComment
from .serializers import UserSer


class SignUp(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        user = User.objects.all()
        ser = UserSer(user, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = UserSer(data=request.data)
        if ser.is_valid():
            user = ser.save()
            send_mail(
                'iPro Service',
                'Assalomu Aleykum',
                settings.EMAIL_HOST_USER,
                [user.email, ]
            )
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)

class LikeNews(APIView):
	def post(self, request, id):
		news = News.objects.get(id=id)
		if Like.objects.filter(news=news):
			like = Like.objects.filter(news=news).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return Response({'message':'Like deleted'})
			like.user.add(request.user)
			return Response({'message':'Like added'})
		like = Like.objects.create(
				news=news
			)
		like.user.add(request.user)
		return Response({'message':'Like added'})


class LikeCommentList(APIView):
	def post(self, request, id):
		comment = Comment.objects.get(id=id)
		if LikeComment.objects.filter(comment=comment):
			like = LikeComment.objects.filter(comment=comment).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return Response({'message':'Like deleted'})
			like.user.add(request.user)
			return Response({'message':'Like added'})
		like = LikeComment.objects.create(
				comment=comment
			)
		like.user.add(request.user)
		return Response({'message':'Like added'})

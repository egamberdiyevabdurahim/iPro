from rest_framework import serializers

from .models import Photo, News, Comment
from User.serializers import UserSer


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo']


class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'photo', 'video', 'user', 'created_at')
        read_only_fields = ['photo']


class NewsGetSer(serializers.ModelSerializer):
    user = UserSer()
    photo = PhotoSer(many=True)
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'photo', 'video', 'user', 'created_at', 'sum_of_likes')


class CommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user', 'news', 'created_at')


class CommentGetSer(serializers.ModelSerializer):
    user = UserSer()
    news = NewsSer()
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user', 'news', 'created_at')
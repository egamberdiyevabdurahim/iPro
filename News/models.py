from email.policy import default
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from User.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='news_photo')


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ManyToManyField(Photo)
    video = models.FileField(upload_to='news_video', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    viewed_list = models.IntegerField(default=0)

    @property
    def sum_of_likes(self):
        return self.like_news.user.count()

    def sum_of_vieved_list(self, *args, **kwargs):
        self.viewed_list = self.viewed_list+1
        super(News, self).save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Like(models.Model):
    news = models.OneToOneField(News, on_delete=models.CASCADE, related_name='like_news')
    user = models.ManyToManyField(User, related_name='like_user')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news.title
    

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comment_news')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def sum_of_likes(self):
        return self.like_comment.user.count()

class LikeComment(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name="like_comment")
    user = models.ManyToManyField(User, related_name="likecomment_user")
    created_at = models.DateTimeField(auto_now_add=True)
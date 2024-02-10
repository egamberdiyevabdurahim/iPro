from django.urls import path

from .views import SignUp, LikeNews, LikeCommentList

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='signin'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('like/<int:id>', LikeNews.as_view(), name='like'),
    path('likecomment/<int:id>', LikeCommentList.as_view(), name='likecomment'),
]

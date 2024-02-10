from django.urls import path

from .views import AllList, PhotoList, NewsList, NewsDetail


urlpatterns = [
    path('all/', AllList.as_view(), name='all'),
    path('photo/', PhotoList.as_view(), name='photo'),
    path('', NewsList.as_view(), name='news'),
    path('<int:id>/', NewsDetail.as_view(), name='news_detail'),
]
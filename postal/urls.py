from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView
    # article_list_view,
    # article_detail_view,
)

app_name = 'postal'
urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='articles'),

    
]

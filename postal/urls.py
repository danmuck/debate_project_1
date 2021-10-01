from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView


    # article_list_view,
    # article_detail_view,
)

app_name = 'postal'
urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('create/', ArticleCreateView.as_view(), name='new-article'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),

    
]

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.urls import reverse
from .models import Article
from .forms import ArticleForm

from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView

)
# Create your views here.

class ArticleListView(ListView):
    queryset = Article.objects.all().order_by('pk') # <app_name>/<model_name>_list.html #this is the default path it looks for template 
    model = Article
    template_name = "postal/article_list.html"

class ArticleDebateView(ListView):
    queryset = Article.objects.get(title__contains='debate').order_by('pk') # <app_name>/<model_name>_list.html #this is the default path it looks for template 
    model = Article
    template_name = "postal/article_debate.html"

class ArticleCreateView(CreateView):
    queryset = Article.objects.all() # <app_name>/<model_name>_create.html #this is the default path it looks for template 
    model = Article
    form_class = ArticleForm
    template_name = "postal/article_create.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "postal/article_detail.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    queryset = Article.objects.all() # <app_name>/<model_name>_update.html #this is the default path it looks for template 
    model = Article
    form_class = ArticleForm
    template_name = "postal/article_update.html"

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "postal/article_delete.html"

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('postal:articles')






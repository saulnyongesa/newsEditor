from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'), # A homepage to list news
    path('create/', views.create_article, name='create_article'),
    path('news/<int:pk>/', views.article_detail, name='article_detail'),
]
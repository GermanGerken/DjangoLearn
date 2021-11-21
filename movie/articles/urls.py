from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_home, name='articles_home'),
    path('create', views.articles_create, name='articles_create'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='full_article'),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name='update_article'),
    path('<int:id>/delete', views.articles_delete, name='delete_article')
]

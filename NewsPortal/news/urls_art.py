from django.urls import path

from .views import PostsList,PostsDetail, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [
   # path('', PostsList.as_view(), name='post_list'),
   # path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]

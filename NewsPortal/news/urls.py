from django.urls import path

from .views import PostsList, PostsDetail, PostSearch, PostCreate, PostUpdate, PostDelete, subscriptions


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]

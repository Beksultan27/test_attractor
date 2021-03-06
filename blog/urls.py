from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/api/', PostList.as_view(), name='post_api'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),

    path('categories/', categories_list, name='categories_list_url'),
    path('categories/api/', CategoryList.as_view(), name='category_api'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('category/<str:slug>/delete', CategoryDelete.as_view(), name='category_delete_url')
]

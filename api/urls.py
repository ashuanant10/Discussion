from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user_home/<int:user_id>/', views.user_home, name='user_home'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('show_users/', views.show_user_list, name='show_user_list'),
    path('search_user/', views.search_user, name='search_user'),

    path('create_post/', views.create_post, name='create_post'),
    path('list_posts/', views.list_post, name='list_post'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment_on_post/<int:post_id>/', views.comment_on_post, name='comment_on_post'),

    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    
    path('list_discussions_by_tags/', views.list_discussions_by_tags, name='list_discussions_by_tags'),
    path('list_discussions_by_text/', views.list_discussions_by_text, name='list_discussions_by_text'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

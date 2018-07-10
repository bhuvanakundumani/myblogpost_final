from django.urls import path
from .views import list_posts, new_post, update_post,post_detail,delete_post

urlpatterns=[

    path('',list_posts, name='list_posts'),
    path('new/',new_post,name ='new_post'),
    path('update/<int:id>/', update_post,name='update_post'),
    path('<int:pk>', post_detail, name ='post_detail' ),
    path('delete/<int:id>/', delete_post, name ='delete_post'),

]

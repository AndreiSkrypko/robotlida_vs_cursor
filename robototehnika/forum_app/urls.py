from django.urls import path
from .views import forum_list, create_post, create_reply

urlpatterns = [
    path('forum_list/', forum_list, name='forum_list'),
    path('create/', create_post, name='create_post'),
    path('reply/<int:post_id>/', create_reply, name='create_reply'),  # ✅ путь для ответов
]

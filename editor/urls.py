from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name='create_post'),
    path('post-list/', views.post_list, name='post_list'),  # Optional: To display the list of posts
]

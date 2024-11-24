from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.PostListView.as_view(), name='api_post_list'),   
    path('api/post/<int:post_id>/', views.PostDetailView.as_view(), name='api_post_detail'),   
    path('api/post/<int:post_id>/response/', views.ResponseCreateView.as_view(), name='api_response_create'),  
    path('api/discussions/', views.DiscussionListView.as_view(), name='api_discussion_list'),  
    path('api/discussion/<int:discussion_id>/', views.DiscussionDetailView.as_view(), name='api_discussion_detail'),   
]

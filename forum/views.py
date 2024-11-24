from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response   
from .models import Post, Discussion, Response as ForumResponse  
from .serializers import PostSerializer, DiscussionSerializer, ResponseSerializer
from rest_framework import status

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()   
        serializer = PostSerializer(posts, many=True)   
        return Response(serializer.data)   


class PostDetailView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)  
        serializer = PostSerializer(post)  
        return Response(serializer.data)  


class ResponseCreateView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class DiscussionListView(APIView):
    def get(self, request):
        discussions = Discussion.objects.all()
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)

class DiscussionDetailView(APIView):
    def get(self, request, discussion_id):
        discussion = get_object_or_404(Discussion, id=discussion_id)
        serializer = DiscussionSerializer(discussion)
        return Response(serializer.data)





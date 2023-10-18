from django.shortcuts import render
from .models import Post
# rest_framework 추가 후 추가된 코드
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import PostSerializer


# FBV 사용 방식
# @api_view(['GET'])
# def postlist(request):
#     posts = [
#         {'title':'1', 'content':'111'},
#         {'title':'2', 'content':'222'},
#         {'title':'3', 'content':'333'},
#     ]
#     serializer = posts
#     return Response(serializer)

# CBV 사용 방식
# class HrulerView(APIView):
#     def get(self, request):
#         posts = [
#             {'title':'1', 'content':'111'},
#             {'title':'2', 'content':'222'},
#             {'title':'3', 'content':'333'},
#         ]
#         serializer = posts
#         return Response(serializer)
    
# postlist = HrulerView.as_view()

@api_view(['GET', 'POST'])
def postlist(request):
    if request.method == 'GET':
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
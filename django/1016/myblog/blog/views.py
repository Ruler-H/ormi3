from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q

class PostList(ListView):
    model = Post
    # template_name = '변경.html'
    ordering = '-pk'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()

        # request의 GET 파라미터에서 'q'를 가져옴
        q = self.request.GET.get('q', '')

        # 'q' 파라미터가 제공됐을 경우, 쿼리셋을 필터링
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q)).distinct()
        return queryset

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postlist')

class PostTest(DetailView):
    model = Post

    def get(self, request):
        return HttpResponse('PostTest get')
    
    def post(self, request):
        return HttpResponse('PostTest post')
    
postlist = PostList.as_view()
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
test = PostTest.as_view()
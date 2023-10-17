from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import TubePost, Comment
from .forms import CommentForm

class TubePostList(ListView):
    model = TubePost
    ordering = '-pk'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()

        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(Q(title__icontains=q)|Q(content__icontains=q)).distinct()
        
        return queryset
    
class TubePostDetail(DetailView):
    model = TubePost

    def post(pk, self):
        tubePost = TubePost.objects.get(pk=self.kwargs['pk'])
        form = CommentForm(self.request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post=tubePost,
                message=form.cleaned_data['message'],
                author=self.request.user,
            )
            c.save()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
        

tube_list = TubePostList.as_view()
tube_detail = TubePostDetail.as_view()
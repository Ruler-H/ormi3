from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import TubePost, Comment, Tag
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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class TubePostCreate(CreateView):
    model = TubePost
    fields = '__all__'
    success_url = reverse_lazy('tube_list')

class TubePostUpdate(UpdateView):
    model = TubePost
    fields = '__all__'
    success_url = reverse_lazy('tube_list')

class TubePostDelete(DeleteView):
    model = TubePost
    success_url = reverse_lazy('tube_list')

def tube_tag(request, tag):
    tubePosts = TubePost.objects.all()
    tagTube = []
    for tubePost in tubePosts:
        tags = tubePost.tags.filter(Q(name__icontains=tag))
        if tags:
            tagTube.append(tubePost)
    return render(request, 'tube/tubepost_list.html', {'object_list':tagTube})

def comment(request, pk):
    tubePost = TubePost.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post = tubePost,
                message = form.cleaned_data['message'],
                author = request.user,
            )
            c.save()
    new_form = CommentForm()
    return render(request, 'tube/tubepost_detail.html', {'object':tubePost, 'form':new_form})
        

tube_list = TubePostList.as_view()
tube_detail = TubePostDetail.as_view()
tube_create = TubePostCreate.as_view()
tube_update = TubePostUpdate.as_view()
tube_delete = TubePostDelete.as_view()
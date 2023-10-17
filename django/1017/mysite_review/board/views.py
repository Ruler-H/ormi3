from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

def board(request):
    posts = Post.objects.all()
    return render(request, 'board/board.html', {'posts':posts})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post=post,
                message=form.cleaned_data['message'],
                author=request.user
            )
            c.save()
    return render(request, 'board/post.html', {'post':post, 'form':form})

def tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'board/board.html', {'posts':posts})
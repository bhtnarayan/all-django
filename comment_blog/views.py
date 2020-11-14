from django.shortcuts import render
from . models import Post, Comment 
from . forms import CommentForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on') 
    context = {
        'posts': posts,
    }
    return render(request, 'comment_blog/blog_index.html', context) 


@login_required
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on') 
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'comment_blog/blog_category.html', context) 

@login_required
def blog_detail(request, pk):
    post = Post.objects.get(pk = pk) 

    form = CommentForm() 
    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post 
            )
            comment.save() 
          
    comments = Comment.objects.filter(post = post) 
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'comment_blog/blog_details.html', context) 


class PostView(CreateView):
    model = Post 
    template_name = "comment_blog/blog_detail_form.html"
    fields = "__all__"
    success_url = "/comment_blog/home"

class PostUpdateView(UpdateView):
    model = Post 
    template_name = "comment_blog/blog_update_form.html"
    fields = "__all__"
    success_url = "/comment_blog/home"

class PostDeleteView(DeleteView):
    model = Post 
    template_name = "comment_blog/blog_delete.html"
    success_url = "/comment_blog/home"
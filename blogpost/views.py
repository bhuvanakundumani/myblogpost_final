from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.

def list_posts(request):
    posts=Post.objects.all()
    return render(request, 'blogposts.html',{'posts':posts})


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'post_detail.html',{'post':post})


def new_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.published_date = timezone.now()
        form.save()
        return redirect(list_posts)

    return render(request,'form.html', {'form': form})

def update_post(request,id):
    post=get_object_or_404(Post,pk=id)
    form=PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(list_posts)
    return render(request,'form.html',{'form':form})

def delete_post(request,id):
    post=get_object_or_404(Post,pk=id)

    if request.method == 'POST':
        post.delete()
        return redirect(list_posts)
    return render(request,'confirm.html',{'post':post})

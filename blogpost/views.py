from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def list_posts(request):
    posts=Post.objects.all()
    return render(request, 'blogposts.html',{'posts':posts})


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'post_detail.html',{'post':post})

@login_required
def new_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.published_date = timezone.now()

        form.save()
        return redirect(list_posts)

    return render(request,'form.html', {'form': form})

@login_required
def update_post(request,id):
    post=get_object_or_404(Post,pk=id)
    form=PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(list_posts)
    return render(request,'form.html',{'form':form})


@login_required
def delete_post(request,id):
    post=get_object_or_404(Post,pk=id)

    if request.method == 'POST':
        post.delete()
        return redirect(list_posts)
    return render(request,'confirm.html',{'post':post})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list_posts')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

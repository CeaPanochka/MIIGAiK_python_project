from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model

from .models import Group, Post
from .forms import PostForm

User = get_user_model()

AMOUNT = 10


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


# Страница с информацией о группе
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:AMOUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {
        'username': username,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    author = get_object_or_404(User, username=post.author)
    count = author.posts.count()
    title = post.text[:30]
    context = {
        'post': post,
        'count': count,
        'title': title,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            return redirect('/posts/thankyou/')

        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def thank_you(request):
    return render(request, 'posts/thankyou.html')


def post_edit(request, post_id):
    post_author = Post.objects.get(id=post_id).author
    current_user = request.user
    is_edit = True

    if current_user == post_author:
        if request.method == 'POST':
            form = PostForm(request.POST)

            if form.is_valid():
                return redirect('/posts/thankyou/')

            return render(request, 'posts/create_post.html', {
                'form': form,
                'is_edit': is_edit,
            })
        form = PostForm()
        return render(request, 'posts/create_post.html', {
            'form': form,
            'is_edit': is_edit,
        })
    else:
        return redirect('/posts/post_detail.html')

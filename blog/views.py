from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Post, Category, Tag
from .forms import CommentForm

def blog_home(request):
    featured_posts = Post.objects.filter(status='published', featured=True)[:3]
    recent_posts = Post.objects.filter(status='published')[:6]
    popular_posts = Post.objects.filter(status='published').order_by('-views')[:5]
    categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)
    
    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'popular_posts': popular_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

def post_list(request):
    post_list = Post.objects.filter(status='published')
    search_query = request.GET.get('search')
    categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)
    popular_posts = Post.objects.filter(status='published').order_by('-views')[:5]
    
    if search_query:
        post_list = post_list.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
    
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'search_query': search_query,
        'categories': categories,
        'popular_posts': popular_posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    post.increment_views()
    
    comments = post.comments.filter(active=True)
    related_posts = Post.objects.filter(
        status='published',
        category=post.category
    ).exclude(pk=post.pk)[:3]
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(status='published', category=category)
    
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'blog/category_posts.html', context)

def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    post_list = Post.objects.filter(status='published', tags=tag)
    
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'tag': tag,
    }
    return render(request, 'blog/tag_posts.html', context)
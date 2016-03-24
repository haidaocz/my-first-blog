from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Comment, Article
from .forms import PostForm, CommentForm, ArticleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 15) # Show 15 posts per page

    page = request.GET.get('page')

    # pagination process
    try:
        posts_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts_page = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts_page})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    paginator = Paginator(posts, 15) # Show 15 posts per page

    page = request.GET.get('page')

    # pagination process
    try:
        posts_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts_page = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_draft_list.html', {'posts': posts_page})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_tags = post.tags.all()

    return render(request, 'blog/post_detail.html', {'post': post, 'tags':post_tags})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            form.save_m2m()   #reserve tags
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()   #reserve tags
            return redirect('blog.views.post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('blog.views.post_detail', slug=post.slug)

# in models.py
# def publish(self):
#     self.published_date = timezone.now()
#     self.save()

@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.POST["author"] # modified by michael
            comment.save()
            return redirect('blog.views.post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', slug=comment.post.slug)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    slug = comment.post.slug
    comment.delete()
    return redirect('blog.views.post_detail', slug=slug)


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            # post.published_date = timezone.now()
            article.save()
            form.save_m2m()   #reserve tags
            return redirect('article_detail', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_edit.html', {'form': form})



def article_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    post_tags = post.tags.all()

    return render(request, 'blog/article_detail.html', {'post': post, 'tags': post_tags})


def tag_articles(request, tag):
    articles = Article.objects.filter(tags__name__in=[tag])
    paginator = Paginator(articles, 15) # Show 15 articles per page
    page = request.GET.get('page')

     # pagination process
    try:
        articles_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles_page = paginator.page(paginator.num_pages)

    return render(request, 'blog/tag_articles.html', {'posts': articles_page})

@login_required
def article_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog.views.article_detail', slug=post.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_edit.html', {'form': form})


@login_required
def article_publish(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.publish()
    return redirect('blog.views.article_detail', slug=article.slug)

@login_required
def article_remove(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('blog.views.article_list')

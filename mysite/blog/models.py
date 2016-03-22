# Create your models here.
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def delete(self):
        self.visible = False
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def delete(self):
        self.visible = False
        self.save()

    def __str__(self):
        return self.text



class Tech(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    source_link1 = models.CharField(max_length=200)
    source_link2 = models.CharField(max_length=200)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    read_time = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Fashion(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    source_link = models.CharField(max_length=200)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    read_time = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    source_link = models.CharField(max_length=200)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    read_time = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



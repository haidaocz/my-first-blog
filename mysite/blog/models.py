# Create your models here.
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True)

    tags = TaggableManager()

    visible = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.id:
            slug_string = (
                str(self.created_date.year), str(self.created_date.month),
                str(self.created_date.day), str(self.title)
            )
            self.slug = slugify(slug_string)
        super(Post, self).save(*args, **kwargs)

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

# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#     visible = models.BooleanField(default=True)
#
#     def delete(self):
#         self.visible = False
#         self.save()
#
#     def __str__(self):
#         return self.name

class Fashion(models.Model):
    author = models.ForeignKey('auth.User')
    # tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=200)
    content = models.TextField()
    source_link = models.CharField(max_length=300)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    read_time = models.CharField(max_length=10)
     # read count
    read_counts = models.IntegerField(default=True)
    slug = models.SlugField(max_length=200, blank=True)
    visible = models.BooleanField(default=True)

    tags = TaggableManager()

    def counts(self):
        self.read_counts += 1
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    # tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=200)
    content = models.TextField()
    source_link = models.CharField(max_length=300)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    read_time = models.CharField(max_length=10)

    # read count
    read_counts = models.IntegerField(default=True)

    slug = models.SlugField(max_length=200, blank=True)
    tags = TaggableManager()

    visible = models.BooleanField(default=True)

    def counts(self):
        self.read_counts += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            slug_string = (
                str(self.created_date.year), str(self.created_date.month),
                str(self.created_date.day), str(self.title)
            )
            self.slug = slugify(slug_string)
        super(Article, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     kwargs = {'year': self.created_date.year,
    #               'month': self.created_date.month,
    #               'day': self.created_date.day,
    #               'slug': self.slug,
    #               'pk': self.pk
    #               }
    #     return reverse('article_detail', kwargs=kwargs)


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

class ArticleComment(models.Model):
    post = models.ForeignKey('blog.Article', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

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
    # tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=200)
    content = models.TextField()
    source_link1 = models.CharField(max_length=300)
    source_link2 = models.CharField(max_length=300)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    read_time = models.CharField(max_length=10)
     # read count
    read_counts = models.IntegerField(default=True)

    slug = models.SlugField(max_length=200, blank=True)
    visible = models.BooleanField(default=True)

    def counts(self):
        self.read_counts += 1
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
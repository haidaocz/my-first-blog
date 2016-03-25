from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/detail/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^article/tag/(?P<tag>[-\w]+)/$', views.tag_articles, name='tag_articles'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^post/(?P<slug>[-\w]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^article/(?P<slug>[-\w]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<slug>[-\w]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<slug>[-\w]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^article/(?P<slug>[-\w]+)/remove/$', views.article_remove, name='article_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^article/detail/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
    # url(r'^search/', include('haystack.urls')),
]



# url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
# url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
# url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)-(?P<slug>[-\w]*)/$', views.article_detail, name='article_detail'),
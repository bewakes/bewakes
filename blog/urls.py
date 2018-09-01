from django.conf.urls import url
from blog.views import (
    Posts, Tags, ImageUpload, CommentProcess, searchresult, Home
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'newblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'posts/$', Posts.as_view(), name='posts'),
    url(r'tags/$', Tags.as_view(), name='tags'),
    url(r'upload-image/$', ImageUpload.as_view(), name='upload-image'),
    url(r'comment/process/$', CommentProcess.as_view(), name='comment'),
    url(r'search/results/$', searchresult, name='searchresult'),
    url(r'(?P<slug>[-a-zA-z0-9]+)/$', Home.as_view(), name='home'),
    url(r'^$', Home.as_view(), name='index'),
]

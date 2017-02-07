from django.conf.urls import include, url
from blog.views import *

urlpatterns =[ 
    # Examples:
    # url(r'^$', 'newblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Home.as_view(), name='index'),
    url(r'^(?P<slug>[-a-zA-z0-9]+)/$', Home.as_view(), name='home'),
    url(r'^comment/process/', CommentProcess.as_view(), name='comment'),
    url(r'^search/results/', searchresult, name='searchresult'),
]

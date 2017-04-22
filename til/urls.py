from django.conf.urls import include, url
from til.views import *

urlpatterns =[ 

    url(r'^$', TILHome.as_view(), name='til-index'),
    url(r'^api/', get_til, name="til-api"),
    #url(r'^(?P<item_id>[0-9]_)/$', 
]

from django.conf.urls import include, url
from journal.views import *

urlpatterns =[ 

    url(r'^$', JournalHome.as_view(), name='journal-index'),
    url(r'^list/', get_journal, name="journal-list"),
]

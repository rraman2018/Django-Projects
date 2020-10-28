from django.conf.urls import url
from cards.views import CardCollection, CardRecord, TasksCollection, TaskRecord

# RESTful specific urls

urlpatterns = [
    url(
        r'cards$',
        CardCollection.as_view()
    ),
    url(
        r'cards/(?P<pk>[0-9]+)$',
        CardRecord.as_view()
    ),
    url(
        r'task$',
        TasksCollection.as_view(),
        name='task-collection'
    )
    ,
    url(
        r'task/(?P<pk>[0-9]+)$',
        TaskRecord.as_view(),
        name='task-record'
    )
]
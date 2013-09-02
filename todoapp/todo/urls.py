from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from api import TaskResource

urlpatterns = patterns('todo.views',
    url(r'^/?$', 'index', name='index'),
    url(r'item/(?P<id>[0-9]+)/$', 'item', name='item'),
    url(r'(?P<id>[0-9]+)/$', 'update_task', name='update_task'),
)

urlpatterns += patterns('',
    url(r'^api/$', TaskResource.as_view(), name='api-products-collection'),
    # url(r'^products/(?P<pk>\d+)/$', ProductResource.as_view(), name='api-products-model'),
)

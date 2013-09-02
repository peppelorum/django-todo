#sliver objects
from sliver.views import ModelResource, CollectionResource
from sliver.mixins import JSONMixin

#your data
from models import Task

class TaskResource(JSONMixin, CollectionResource):
    model = Task
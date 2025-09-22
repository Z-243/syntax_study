from rest_framework.serializers import ModelSerializer
from base.models import Room


# serializers are classes that take a model object and convert it to Json(Response method in views.py doesn't work on objects)


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

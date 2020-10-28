from rest_framework import serializers
from cards.models import Card, Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-record'
    )

    status_text = serializers.SerializerMethodField()

    def get_status_text(self, instance):
        return instance.get_status_display()

    class Meta:
        model = Card
        fields = '__all__'
        extra_kwargs = {
            'status': {'write_only': True}
        }

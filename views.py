from rest_framework import generics, permissions
from cards.models import Card, Tasks
from cards.serializers import CardSerializer, TaskSerializer
from cards.util import custom_permissions

class CardCollection(generics.ListCreateAPIView): # GET, POST
    #queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(
            owner=self.request.user     # John and Jack can only see thier own cards
        )
    # only authenticated users can create account
    permission_classes = [
        custom_permissions.IsOwner
    ]
    # add owner info
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CardRecord(generics.RetrieveUpdateDestroyAPIView): # UPDATE, DELETE
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [
        custom_permissions.IsOwner
    ]

class TasksCollection(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from message.models import Chat_room, Message
from message.serializers import Chat_roomSerializer, MessageSerializer


class Chat_roomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chat_room.objects.all()
    serializer_class = Chat_roomSerializer

    def get_queryset(self):
        chatrooms = Chat_room.objects.filter(users=self.request.user)
        return chatrooms


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import get_messages_for_user
from .serializers import MessageSerializer, MessageRetrieveSerializer
from .permissions import IsSenderOrReceiver
from .models import Message


class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'GET':
            return MessageRetrieveSerializer
        return MessageSerializer

    def get_queryset(self):
        """
        Overriden `get_query_set` method, which is to be used in `list` method later, 
        so as to get all messages sent to a particular user.
        """
        return get_messages_for_user(self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all().select_related('sender', 'receiver')
    serializer_class = MessageRetrieveSerializer
    permission_classes = (IsAuthenticated, IsSenderOrReceiver)

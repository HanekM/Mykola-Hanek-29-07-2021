from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MessageSerializer, MessageRetrieveSerializer
from .models import Message


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all().select_related('sender', 'receiver')
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'GET':
            return MessageRetrieveSerializer
        return MessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

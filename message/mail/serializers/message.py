from rest_framework import serializers

from user.serializers import UserSerializer
from mail.models import Message


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'subject', 'message')


class MessageRetrieveSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'subject', 'message', 'date_created')

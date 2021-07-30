from typing import Iterable

from django.contrib.auth import get_user_model

from mail.models import Message


def get_messages_for_user(user: get_user_model) -> Iterable[Message]:
    """
    Returns all the messages sent to a particular user by 'related_name'
    """
    return user.messages_obtained.all()

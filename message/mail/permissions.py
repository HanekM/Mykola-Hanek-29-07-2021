from rest_framework.permissions import BasePermission


class IsSenderOrReceiver(BasePermission):
    """
    Checks whether the user who requested the message is either sender or receiver.
    """

    def has_permission(self, request, view):
        message = view.get_object()
        return request.user == message.sender or request.user == message.receiver

from rest_framework.permissions import BasePermission


class IsReceiver(BasePermission):
    """
    Checks whether the user who requested the message is an intended receiver.
    """

    def has_permission(self, request, view):
        return request.user == view.get_object().receiver

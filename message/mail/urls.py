from django.urls import path

from .views import MessageListCreateAPIView, MessageRetrieveDestroyAPIView

app_name = 'mail'

urlpatterns = [
    # api/messages/
    path('', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('<int:pk>/', MessageRetrieveDestroyAPIView.as_view(), name='message-retrieve-destoy')
]

from django.urls import path
from rest_framework_simplejwt import views

from .views import MessageListCreateAPIView

app_name = 'mail'

urlpatterns = [
    # api/messages/
    path('', MessageListCreateAPIView.as_view(), name='message-list-create')
    
]

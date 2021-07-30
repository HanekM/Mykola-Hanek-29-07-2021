from django.urls import path
from rest_framework_simplejwt import views


app_name = 'user'

urlpatterns = [
    # api/users/
    path('token/', views.TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token-refresh')
]

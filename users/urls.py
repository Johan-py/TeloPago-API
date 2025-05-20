from django.urls import path
from .views import UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import user_profile

urlpatterns = [
    path('createusers/', UserCreateAPIView.as_view(), name='user-create'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', user_profile, name='user-profile'),

]

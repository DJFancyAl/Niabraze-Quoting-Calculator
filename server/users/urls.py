from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ProtectedView, LogoutView, UserView

urlpatterns = [
    path('', UserView.as_view(), name='user-view'),
    path('protected/', ProtectedView.as_view(), name='protected-view'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
]
from django.urls import path
from .views import ProtectedView, LoginView, LogoutView, UserView

urlpatterns = [
    path('', UserView.as_view(), name='user-view'),
    path('protected/', ProtectedView.as_view(), name='protected-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
]
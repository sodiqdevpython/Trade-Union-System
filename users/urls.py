from django.urls import path
from users import views

urlpatterns = [
    path("singup/", views.UserRegisterAPIView.as_view(), name="signup"),
    path("login/", views.UserLoginAPIView.as_view(), name="login"),
    path("profile/", views.UserProfileAPIView.as_view(), name="profile"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout")
]

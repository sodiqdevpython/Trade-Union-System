from rest_framework.routers import DefaultRouter
from .views import (
    OrganizationViewSet,
    EventView,
    ApplicationView,
    SpiritualRestView,
    AccidentsView
)
from django.urls import path, include
from api import views

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'spirtual-rest', SpiritualRestView)
router.register(r'accident', AccidentsView)


urlpatterns = [
    path("singup/", views.UserRegisterAPIView.as_view(), name="signup"),
    path("login/", views.UserLoginAPIView.as_view(), name="login"),
    path("profile/", views.UserProfileAPIView.as_view(), name="profile"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout"),
    path('', include(router.urls)),
    path('event/', EventView.as_view()),
    path('event/<int:id>/', EventView.as_view()),
    path('application/', ApplicationView.as_view()),
    path('application/<int:id>/', ApplicationView.as_view())
]
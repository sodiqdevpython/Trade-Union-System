from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrganizationViewSet,
    EventView,
    ApplicationView,
    SpiritualRestView,
    AccidentsView
)


router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'spirtual-rest', SpiritualRestView)
router.register(r'accident', AccidentsView)

urlpatterns = [
    path('', include(router.urls)),
    path('event/', EventView.as_view()),
    path('event/<int:id>/', EventView.as_view()),
    path('application/', ApplicationView.as_view()),
    path('application/<int:id>/', ApplicationView.as_view())
]

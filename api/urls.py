from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UnderAgeChildrenViewSet, HandicappedDocsModelViewSet, RoleNoteModelViewSet,
    JobViewSet, EmployeeViewSet, OrganizationViewSet, IDCardViewSet,
    EventView, ApplicationView, SpiritualRestView, AccidentsView
)


router1 = DefaultRouter()
router1.register(r'under_age_children', UnderAgeChildrenViewSet)
router1.register(r'handicapped_docs', HandicappedDocsModelViewSet)
router1.register(r'role_notes', RoleNoteModelViewSet)
router1.register(r'jobs', JobViewSet)
router1.register(r'employees', EmployeeViewSet)

router2 = DefaultRouter()
router2.register(r'organizations', OrganizationViewSet)
router2.register(r'id-cards', IDCardViewSet)
router2.register(r'spirtual-rest', SpiritualRestView)
router2.register(r'accident', AccidentsView)

urlpatterns = [
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('event/', EventView.as_view()),
    path('event/<int:id>/', EventView.as_view()),
    path('application/', ApplicationView.as_view()),
    path('application/<int:id>/', ApplicationView.as_view())
]

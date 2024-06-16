from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnderAgeChildrenViewSet, HandicappedDocsModelViewSet, RoleNoteModelViewSet, JobViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'under_age_children', UnderAgeChildrenViewSet)
router.register(r'handicapped_docs', HandicappedDocsModelViewSet)
router.register(r'role_notes', RoleNoteModelViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

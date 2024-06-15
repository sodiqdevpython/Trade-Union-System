from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:id>/', EmployeeView.as_view())
]
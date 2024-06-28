from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile_update/<int:id>/', views.profile_update, name='profile_update'),
    path('filling_info/', views.filling_info, name='filling_info'),
]
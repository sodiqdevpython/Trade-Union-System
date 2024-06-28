from django.urls import path
from .views import (
    dashboard, profile, tables,
    billing, user_profile, verify_user,
    create_event, event_detail
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('tables/', tables, name='tables'),
    path('billing/', billing, name='billing'),
    path('user-profile/<str:id_card>/', user_profile, name='user_profile'),
    path('verify/<int:id>/', verify_user, name='verify_user'),
    path('createcreate_event/', create_event, name='create_event'),
    path('event/<int:id>/', event_detail, name='event_detail')
]
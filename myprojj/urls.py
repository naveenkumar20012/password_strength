from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_check/', views.password_check, name='password_check'),
    path('password_check_result/<int:password_check_id>/', views.password_check_result, name='password_check_result'),
    path('password_check_history/', views.password_check_history, name='password_check_history'),
    path('password_check_delete/<int:password_check_id>/', views.password_check_delete, name='password_check_delete'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]

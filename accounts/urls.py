from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('<int:user_id>/profile', views.UserProfileView.as_view(), name='user_profile'),
    path('<int:user_id>/logout', views.UserLogoutView.as_view(), name='user_logout'),

]

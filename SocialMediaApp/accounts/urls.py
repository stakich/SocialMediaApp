from django.urls import path, include
from SocialMediaApp.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),

]

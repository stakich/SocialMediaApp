from django.urls import include, path
from SocialMediaApp.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
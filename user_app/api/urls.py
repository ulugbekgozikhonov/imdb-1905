from django.urls import path
from rest_framework.authtoken import views

from user_app.api.views import register

urlpatterns = [
	path('login/', views.obtain_auth_token),
	path('register/', register),
]

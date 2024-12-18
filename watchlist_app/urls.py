from django.urls import path

from .views import WatchListAPIView, StreamPlatformAPIView, ReviewAV

urlpatterns = [
	path('watchlist/', WatchListAPIView.as_view()),
	path('review/<int:pk>', ReviewAV.as_view()),
	path('stream/', StreamPlatformAPIView.as_view()),
]

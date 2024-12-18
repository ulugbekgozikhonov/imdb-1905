from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.models import StreamPlatform, WatchList, Review
from watchlist_app.permessions import IsAdminOrAuthenticatedForOnlyRead
from watchlist_app.serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer


class WatchListAPIView(generics.ListCreateAPIView):
	queryset = WatchList.objects.all()
	serializer_class = WatchListSerializer
	permission_classes = [IsAdminOrAuthenticatedForOnlyRead]


class ReviewAV(generics.ListCreateAPIView):
	serializer_class = ReviewSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Review.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		pk = self.kwargs['pk']
		watchlist = WatchList.objects.get(pk=pk)

		review = Review.objects.filter(watchlist=watchlist, user=self.request.user)

		if review.exists():
			raise ValidationError("Your review is already exists")

		if watchlist.rating == 0:
			watchlist.rating = serializer.validated_data['rating']
		else:
			watchlist.rating = (watchlist.rating + serializer.validated_data['rating']) / 2

		watchlist.rating_count += 1
		watchlist.save()

		serializer.save(user=self.request.user, watchlist=watchlist)


class StreamPlatformAPIView(APIView):

	def get(self, request):
		stream_platform = StreamPlatform.objects.all()
		serializer = StreamPlatformSerializer(instance=stream_platform, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StreamPlatformSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

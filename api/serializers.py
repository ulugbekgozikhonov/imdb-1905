from rest_framework import serializers

from api.models import WatchList, StreamPlatform, Review


class StreamPlatformSerializer(serializers.ModelSerializer):
	# watchlist = WatchListSerializer(many=True, read_only=True)

	class Meta:
		model = StreamPlatform
		fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
	stream = StreamPlatformSerializer(read_only=True)

	class Meta:
		model = WatchList
		fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	watchlist = WatchListSerializer(read_only=True)

	class Meta:
		model = Review
		fields = ["id", "description", "rating", "watchlist"]

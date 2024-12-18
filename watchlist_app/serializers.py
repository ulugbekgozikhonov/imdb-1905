from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from watchlist_app.models import WatchList, StreamPlatform, Review


class StreamPlatformSerializer(serializers.ModelSerializer):
	# watchlist = WatchListSerializer(many=True, read_only=True)

	class Meta:
		model = StreamPlatform
		fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
	stream = StreamPlatformSerializer(read_only=True)
	rating = serializers.ReadOnlyField()
	rating_count = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()

	class Meta:
		model = WatchList
		fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
	watchlist = StringRelatedField(read_only=True)
	user = StringRelatedField(read_only=True)

	class Meta:
		model = Review
		fields = "__all__"

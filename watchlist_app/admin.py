from django.contrib import admin

from watchlist_app.models import WatchList, StreamPlatform, Review

admin.site.register(WatchList)


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
	list_display = ['id', 'website', 'about']


admin.site.register(Review)

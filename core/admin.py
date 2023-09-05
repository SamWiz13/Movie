from django.contrib import admin

from .models import WatchList, StreamPlatform, Review


class StreamPlatformAdmin(admin.ModelAdmin):
    list_display =('name', 'about')



class MovieAdmin(admin.ModelAdmin):
    list_display =('title','active')


class ReviewAdmin(admin.ModelAdmin):
    list_display =('rating','watchlist','active')



admin.site.register(StreamPlatform, StreamPlatformAdmin)
admin.site.register(WatchList, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
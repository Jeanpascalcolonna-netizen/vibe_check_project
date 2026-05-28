from django.contrib import admin
from .models import RedditPost

@admin.register(RedditPost)
class RedditPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subreddit', 'score', 'num_comments', 'created_utc']
    list_filter = ['subreddit']
    search_fields = ['title', 'author']
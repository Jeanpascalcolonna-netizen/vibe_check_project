from django.db import models

class RedditPost(models.Model):
    reddit_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    subreddit = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)
    url = models.URLField()
    created_utc = models.DateTimeField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:60]

    class Meta:
        ordering = ['-created_utc']
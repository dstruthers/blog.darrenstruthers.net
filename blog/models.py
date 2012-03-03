from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    """
    Represents one post on the blog.
    """
    title = models.TextField(blank=False)
    slug = models.SlugField(blank=False)
    content = models.TextField(blank=False)
    draft = models.BooleanField(default=True)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    published = models.DateTimeField()

    def __unicode__(self):
        return '%s - %s' % (self.title, str(self.created))

class Comment(models.Model):
    """
    Represents a comment on an Article
    """
    title = models.TextField()
    content = models.TextField(blank=False)
    article = models.ForeignKey(Article)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s / %s' % (self.article, str(self.created))

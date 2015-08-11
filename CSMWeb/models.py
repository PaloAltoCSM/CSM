from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tag(models.Model):
    text = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "Tag #%s" % (self.text)

class Project(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='projmembers')
    followers = models.ManyToManyField(User, related_name='projfollowers')

    # tags
    tags = models.ManyToManyField(Tag)

    def getDict(self):
        return {'id': self.id, 'title': self.title, 'description': self.description}

    def __unicode__(self):
        return "Project #%s" % (self.name)


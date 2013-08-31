from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    amazon_link = models.URLField()
    isbn = models.IntegerField()
    page_count = models.IntegerField()

class Club(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User, through='Membership')
    books = models.ManyToManyField(Book, through='Reading')

class Membership(models.Model):
    user = models.ForeignKey(User)
    club = models.ForeignKey(Club)
    join_date = models.DateField()

class Reading(models.Model):
    book = models.ForeignKey(Book, editable=False)
    club = models.ForeignKey(Club, editable=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    accepted = models.BooleanField(default=False)

class Comment(models.Model):
    '''Note that this can be used like a checkin -- what page am I on
       the editable=False removes it from forms...'''
    user = models.ForeignKey(User, editable=False)
    club = models.ForeignKey(Club)
    book = models.ForeignKey(Book)
    page = models.IntegerField()
    comment = models.TextField()
    curr_date = models.DateField(default=datetime.now(), editable=False)


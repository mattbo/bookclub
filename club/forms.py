from django import forms
from club import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book

class ReadingForm(forms.ModelForm):
    class Meta:
        model = models.Book

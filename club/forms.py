from django import forms
from club import models
from bootstrap_toolkit import widgets

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        widgets = { 'club' : forms.HiddenInput,
                    'book' : forms.HiddenInput}

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book

class ReadingForm(forms.ModelForm):
    class Meta:
        model = models.Reading
        widgets = { 'start_date' : widgets.BootstrapDateInput(),
                    'end_date' : widgets.BootstrapDateInput()}

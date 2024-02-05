#Form definition

from django import forms
from books.models import Book
class Bookform(forms.ModelForm):

    class Meta:

        model=Book
        fields="__all__"
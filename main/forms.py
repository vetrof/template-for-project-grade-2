from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from main.models import Article


class ArticleForm(forms.ModelForm):
    # text = SummernoteTextField()
    class Meta:
        model = Article
        fields = ['text']
        widgets = {
            'text': SummernoteWidget(),
        }


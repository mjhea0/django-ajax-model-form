from django import forms
from ajax.models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        widgets = {
            'title': forms.TextInput(attrs={'id': 'post-title', 'required': True}),
            'description': forms.TextInput(attrs={'id': 'post-desc', 'required': True}),
        }

from django import forms
from .models import Announce, Response, Mailer



class AnnounceForm(forms.ModelForm):
    class Meta:
        model = Announce
        fields = [
            'title',
            'content',

            'category',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'content',
            'announce',
        ]


class AcceptForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'accepted',
        ]


class SendingNewsForm(forms.ModelForm):
    class Meta:
        model = Mailer
        fields = [
            'announce',
            'message'
        ]

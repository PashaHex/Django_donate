from django import forms
from django.core.validators import MinLengthValidator


class DonateCommentForm(forms.Form):
    comment = forms.Field(
        validators=[
            MinLengthValidator(5)
        ]
    )
from django import forms
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator


class DonateCommentForm(forms.Form):

    estimate = forms.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    comment = forms.Field(
        widget=forms.Textarea,
        validators=[
            MinLengthValidator(5)
        ]
    )
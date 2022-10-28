from django import forms
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db.models import F

from donations.models import Item, Office


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


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ('state', 'office')


class OfficeForm(forms.Form):
    office = forms.ModelChoiceField(
        queryset=Office.objects.all()
    )














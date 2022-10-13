from django import forms


class DonateCommentForm(forms.Form):
    comment = forms.Field()
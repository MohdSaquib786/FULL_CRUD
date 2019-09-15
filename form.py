from django import forms
from django.core.exceptions import ValidationError

from onetooneapp.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['user','designation','country']

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        user=self.cleaned_data['user']
        country = self.cleaned_data['country']
        if Profile.objects.filter(user=user).exists():
            raise forms.ValidationError("user alreadyes exist")
        if Profile.objects.filter(country=country).exists():
            raise forms.ValidationError("country already exist")
        return cleaned_data






from django.forms import ModelForm
from .models import Account


class AccountForm(ModelForm):
    def save(self, user, commit=True):
        instance = super(AccountForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Account
        exclude = ['user']

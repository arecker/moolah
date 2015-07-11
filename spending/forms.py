from django import forms
from .models import (
    Transaction,
    Budget,
    Period
)


class MonthlyTransactionForm(forms.ModelForm):
    def save(self, user, budget_pk, commit=True):
        instance = super(
            MonthlyTransactionForm, self).save(commit=False)
        instance.user = user
        instance.budget = Budget.objects.get(pk=budget_pk)
        instance.reason = 1
        instance.negative = True
        instance.period = Period.objects.filter(
            reoccuring=instance.budget.reoccuring).latest()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Transaction
        exclude = ['user', 'budget', 'period', 'reason', 'negative']

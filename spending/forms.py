from django import forms
from .models import (
    MonthlyTransaction,
    MonthlyBudget,
    MonthlyPeriod
)


class MonthlyTransactionForm(forms.ModelForm):
    def save(self, user, budget_pk, commit=True):
        instance = super(
            MonthlyTransactionForm, self).save(commit=False)
        instance.user = user
        instance.budget = MonthlyBudget.objects.get(pk=budget_pk)
        instance.reason = 1
        instance.negative = True
        instance.period = MonthlyPeriod.objects.latest()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = MonthlyTransaction
        exclude = ['user', 'budget', 'period', 'reason', 'negative']

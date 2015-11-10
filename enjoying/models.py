from django.db import models
from django.contrib.auth.models import User

from moolah.models import TransactionBase, TransactionBaseQuerySet
from moolah.utils import get_timestamp, to_decimal


class AllowanceQueryset(models.QuerySet):
    def user(self, user=None):
        return self.filter(user=user).first()

    def current_user(self, request):
        return self.user(request.user)

    def open_period(self):
        for allowance in self.all():
            Purchase.objects.create_from_allowance(allowance)


class Allowance(models.Model):
    objects = AllowanceQueryset.as_manager()

    user = models.OneToOneField(User)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def user_name(self):
        return self.user.get_full_name()

    def __unicode__(self):
        return '{} - {}'.format(self.user_name,
                                to_decimal(self.amount))


class PurchaseQuerySet(TransactionBaseQuerySet):
    def by_allowance(self, allowance):
        return self.filter(allowance=allowance)

    def create_from_allowance(self, allowance):
        date = get_timestamp().strftime("%m/%d/%Y")
        amount = self.by_allowance(allowance).total() + allowance.amount
        desc = 'Allowance for {name} - {date}'.format(date=date,
                                                      name=allowance.user_name)
        return Purchase(amount=amount,
                        description=desc,
                        allowance=allowance).save()


class Purchase(TransactionBase):
    objects = PurchaseQuerySet.as_manager()

    allowance = models.ForeignKey(Allowance, null=True)

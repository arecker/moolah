from django.db import models
from django.contrib.auth.models import User

from moolah.models import TransactionBase


class Purchase(TransactionBase):
    user = models.ForeignKey(User)

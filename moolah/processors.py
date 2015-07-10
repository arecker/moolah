from django.conf import settings
from spending.models import MonthlyBudget
import itertools


def user_theme(request):
    """
    get user's theme if available
    """
    try:
        CSS_THEME_URL = request.user.account.theme.url
    except AttributeError:
        CSS_THEME_URL = settings.DEFAULT_THEME

    return {
        'CSS_THEME_URL': CSS_THEME_URL
    }


def nav_bar(request):
    return {
        'BUDGETS': itertools.chain(MonthlyBudget.objects.all())
    }

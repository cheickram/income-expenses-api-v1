from django.urls import path

from .views import ExpensesSummaryStats
from .views import IncomeSourcesSummaryStats


urlpatterns = [
    path('expense-category-data/', ExpensesSummaryStats.as_view(), name='expense-category-data'),
    path('income-sources-data/', IncomeSourcesSummaryStats.as_view(), name='income-sources-data'),
]
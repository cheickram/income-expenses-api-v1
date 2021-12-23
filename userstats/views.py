from rest_framework.views import APIView
from rest_framework import status, response
import datetime

from expenses.models import Expense
from income.models import Income


class ExpensesSummaryStats(APIView):
    
    def get_category(self, expense):
        return expense.category
    
    def get_amount_for_category(self, expenses_list, category):
        expenses = expenses_list.filter(category=category)
        amount = 0
        
        for expense in expenses:
            amount += expense.amount
            
        return {'amount': str(amount)}
    
    def get(self, request):
        todays_date = datetime.date.today()
        a_year_ago = todays_date - datetime.timedelta(days=365)
        expenses = Expense.objects.filter(owner=request.user.id, date__gte=a_year_ago, date__lte=todays_date)
        
        final = {}
        
        categories = list(set(map(self.get_category, expenses)))
        
        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expenses, category)
                
        return response.Response({'category_data': final}, status=status.HTTP_200_OK)


class IncomeSourcesSummaryStats(APIView):
    
    def get_source(self, incomes):
        return incomes.source
    
    def get_amount_for_source(self, income_list, source):
        incomes = income_list.filter(source=source)
        amount = 0
        
        for income in incomes:
            amount += income.amount
            
        return {'amount': str(amount)}
    
    def get(self, request):
        todays_date = datetime.date.today()
        a_year_ago = todays_date - datetime.timedelta(days=365)
        incomes = Income.objects.filter(owner=request.user.id, date__gte=a_year_ago, date__lte=todays_date)
        
        final = {}
        
        sources = list(set(map(self.get_source, incomes)))
        
        for income in incomes:
            for source in sources:
                final[source] = self.get_amount_for_source(incomes, source)
                
        return response.Response({'income_source_data': final}, status=status.HTTP_200_OK)
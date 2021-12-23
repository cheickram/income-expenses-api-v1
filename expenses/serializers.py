from django.db.models import fields
from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ('id', 'date', 'amount', 'description', 'category')
        
        
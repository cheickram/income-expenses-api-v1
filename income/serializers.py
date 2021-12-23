from django.db.models import fields
from rest_framework import serializers

from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Income
        fields = ('id', 'date', 'amount', 'description', 'source')
        
        
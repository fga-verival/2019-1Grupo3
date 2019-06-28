from django import forms
from .models import TransactionalFunction

class TransactionFunctionForm(forms.ModelForm):
    class Meta:
        model = TransactionalFunction
        fields = ('functionalityName', 'functionalityType', 'qtdALR', 'qtdDER', 'functionComplexity', 'qtdFunctionPts', 'countName')
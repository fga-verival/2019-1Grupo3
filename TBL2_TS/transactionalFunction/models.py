from django.db import models

# Create your models here.

class TransactionalFunction(models.Model):
    functionalityName = models.CharField(max_length=100, blank=False)
    choices_functionalityType = (
        ('EE', 'EE'),
        ('CE', 'CE'),
        ('SE', 'SE')
    )
    functionalityType = models.CharField(
        max_length=2,
        blank=False,
        choices=choices_functionalityType,
    )
    qtdALR = models.PositiveIntegerField(blank=False)
    qtdDER = models.PositiveIntegerField(blank=False)
    functionComplexity = models.CharField(max_length= 5, blank=False)
    qtdFunctionPts = models.PositiveIntegerField(blank=False)
    countName = models.CharField(max_length=100, blank=False)
    registrationDate = models.DateField(auto_now_add=True)
from django.db import models

# Create your models here.
class balance(models.Model):
    amount=models.FloatField(default=None)


class update_balance(models.Model):
    new_balance=models.FloatField()
    def __str__(self):
        return str(float(self.new_balance))


class expences(models.Model):
    expence=models.CharField(max_length=50,default=None)
    pay= models.FloatField(default=None)
    date=models.DateField(default=None)
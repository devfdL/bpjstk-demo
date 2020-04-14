from django.db import models

# Create your models here.
class paymentData(models.Model):
    costumer_id  = models.CharField(max_length=120) 
    source  = models.CharField(max_length=120)
    target  = models.CharField(max_length=120)#
    date  = models.CharField(max_length=120)
    time  = models.CharField(max_length=120)
    amount  = models.CharField(max_length=120)#
    transaction_sign  = models.CharField(max_length=255)

    def __str__(self):
        return '{}, {}'.format(self.source,self.target)
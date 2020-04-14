from django.db import models

# Create your models here.
class DataUser(models.Model):
    nik   = models.CharField(max_length=120)
    user_name = models.CharField(max_length=120)
    alamat   = models.CharField(max_length=255)
    ttl   = models.CharField(max_length=120)
    pekerjaan   = models.CharField(max_length=120)
    user_signature   = models.CharField(max_length=255) # <sha.256(customer data + secret key)encode base64>,
    hp_number = models.CharField(max_length=120)

    def __str__(self):
        return '{}, {}'.format(self.nik,self.user_name)

class walletData(models.Model):
    user_name = models.CharField(max_length=120)
    wallet = models.CharField(max_length=120)
    point = models.CharField(max_length=120)
    last_transaction = models.CharField(max_length=120)

    def __str__(self):
        return '{}, {}'.format(self.id,self.user_name)
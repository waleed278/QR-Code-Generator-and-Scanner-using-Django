from django.db import models

# Create your models here.
class QRCode(models.Model):
    data = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    qr_filename = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.mobile_number
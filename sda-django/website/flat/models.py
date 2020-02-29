from django.db import models

# Create your models here.
class Flat(models.Model):
    code = models.CharField(max_length=20)
    url = models.TextField(max_length=200)
    title = models.CharField(max_length=200)
    rooms = models.PositiveSmallIntegerField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    price_m2 = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    district = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.price} zł - {self.area} m2"

    class Meta:
        verbose_name = "Mieszkanie"
        verbose_name_plural = "Mieszkania"


from django.db import models

# Create your models here.
class Tender(models.Model):

    ref_number = models.CharField( max_length=70)
    title = models.CharField( max_length=100)
    price = models.CharField( max_length=50)
    date = models.DateField()
    dateline = models.DateField()

    class Meta:
        verbose_name = ("Tender")
        verbose_name_plural = ("Tenders")

    def __str__(self):
        return self.title

    

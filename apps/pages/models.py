from django.db import models

# Create your models here.
class Vegatebles(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_ad = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Sabzavot'
        verbose_name_plural = 'Sabzavotlar'
 
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    is_valid = models.BooleanField(default=False)
    created_ad = models.DateField(auto_now=True)

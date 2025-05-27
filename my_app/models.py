from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Tea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tea_detail', kwargs={'tea_id': self.id})
    
class Brewing(models.Model):
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    date = models.DateField('Brewing Date')
    temperature = models.IntegerField(help_text='Temperature in Fahrenheit')
    steeping_time = models.CharField(max_length=20)  # e.g., "3 minutes"
    amount = models.IntegerField(help_text='Amount in grams')
    water_amount = models.IntegerField(help_text='Water amount in ml')

    def __str__(self):
        return f'{self.tea.name} - {self.temperature}°F for {self.steeping_time}'
    
    class Meta:
        ordering = ['-date']

class Teaware(models.Model):
    TEAWARE_TYPES = [
        ('teapot', 'Teapot'),
        ('gaiwan', 'Gaiwan'),
        ('cup', 'Tea Cup'),
        ('infuser', 'Tea Infuser'),
        ('dripper', 'Tea Dripper'),
        ('kettle', 'Kettle'),
        ('tray', 'Tea Tray'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TEAWARE_TYPES)
    material = models.CharField(max_length=50)  # e.g., "Clay", "Porcelain", "Glass"
    capacity = models.IntegerField(help_text='Capacity in ml', null=True, blank=True)
    image = models.ImageField(upload_to='teaware/', blank=True) 
    teas = models.ManyToManyField(Tea, blank=True, related_name='teaware')
    
    def __str__(self):
        return f'{self.name} ({self.get_type_display()})'
    
    def get_absolute_url(self):
        return reverse('teaware_detail', kwargs={'pk': self.id})
    
    class Meta:
        ordering = ['name']
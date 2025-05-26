from django.contrib import admin
from .models import Tea, Brewing, Teaware

# Register your models here.
# This code registers the model with the Django admin site, allowing it to be managed through the admin interface.

admin.site.register(Tea)
admin.site.register(Brewing)
admin.site.register(Teaware)

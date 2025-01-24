from django.contrib import admin
from .models import testModel
# Register your models here.
# now we are connecting our modles to admin panel 

# registering the model in db
admin.site.register(testModel)

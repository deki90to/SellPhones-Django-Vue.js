from django.contrib import admin
from . models import Brand, Specs, Model
# Register your models here.

admin.site.register(Brand)
admin.site.register(Specs)
admin.site.register(Model)
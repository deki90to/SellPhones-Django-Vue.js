from django.contrib import admin
from . models import Brand, Model, Specs
# Register your models here.

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Specs)
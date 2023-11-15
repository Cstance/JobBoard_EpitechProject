from django.contrib import admin
from database import models

admin.site.register(models.Users)
admin.site.register(models.Advertisements)
admin.site.register(models.Companies)
admin.site.register(models.Application)
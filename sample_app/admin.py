from django.contrib import admin
from sample_app.models import AppUser,Packages

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Packages)


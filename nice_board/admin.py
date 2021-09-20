from django.contrib import admin
from .models import NiceThread, NiceComments

admin.site.register(NiceThread)
admin.site.register(NiceComments)

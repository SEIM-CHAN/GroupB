from django.contrib import admin
from .models import NiceThread, NiceComment

admin.site.register(NiceThread)
admin.site.register(NiceComment)

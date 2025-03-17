from django.contrib import admin
from my_app.models import Tag, Example
# Register your models here.

classes = (Tag, Example)
admin.site.register(classes)
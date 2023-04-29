from django.contrib import admin
from .models import Room, Topic, Messaage

# Register your models here.
admin.site.register(Room)
admin.site.register(Messaage)
admin.site.register(Topic)

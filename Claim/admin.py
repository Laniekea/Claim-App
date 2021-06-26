from django.contrib import admin
from .models import  User, Vehicle, Loss, Document, Claim

admin.site.register(Vehicle)
admin.site.register(User)
admin.site.register(Loss)
admin.site.register(Document)
admin.site.register(Claim)
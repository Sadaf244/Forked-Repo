from django.contrib import admin
from .models import Medicine,Patient,Docter,User

# Register your models here.
admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(Patient)
admin.site.register(Docter)
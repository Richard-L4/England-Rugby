from django.contrib import admin
from .models import Contact, Register

# Register your models here.
admin.site.register(Contact)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address')

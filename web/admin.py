from django.contrib import admin

# Register your models here.
from .models import Flan, ContactForm

admin.site.register(Flan)
admin.site.register(ContactForm)

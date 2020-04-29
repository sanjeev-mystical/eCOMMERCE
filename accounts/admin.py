from django.contrib import admin
from .models import GuestEmail
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(GuestEmail)
admin.site.register(User)
from django.contrib import admin
from .models import RegisterUser

@admin.register(RegisterUser)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "password", "is_staff", "is_superuser"]
    fields = ("username", "email", "password", "is_staff", "is_superuser")

    def save_model(self, request, obj, form, change):
        obj.is_staff=True
        obj.is_superuser=True
        raw_password = form.cleaned_data.get("password")
        if raw_password:
            if not (raw_password.startswith("pbkdf2_") or raw_password.startswith("argon2$") or raw_password.startswith("bcrypt")):
                obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

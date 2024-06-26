from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    add_form= CustomUserCreationForm
    form =CustomUserChangeForm
    model=CustomUser
    list_display = ['username', 'email', 'is_staff']

admin.site.register(CustomUser,CustomUserAdmin)
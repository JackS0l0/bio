# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from .models import days_until_expiration  # Убедитесь, что импортируете правильно

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'days_left')

    def days_left(self, obj):
        # Вызываем функцию, чтобы получить оставшиеся дни
        return days_until_expiration(obj)
    days_left.short_description = 'Осталось дней'

# Переопределяем стандартный UserAdmin
admin.site.unregister(User)  # Убираем стандартный UserAdmin
admin.site.register(User, UserAdmin)  # Регистрируем наш кастомный UserAdmin

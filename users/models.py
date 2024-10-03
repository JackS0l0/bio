from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def days_until_expiration(user):
    # Рассчитываем дату окончания срока действия (через 1 год)
    expiration_date = user.date_joined + timezone.timedelta(days=365)
    remaining_days = (expiration_date - timezone.now()).days
    
    # Возвращаем оставшиеся дни, если они больше 0, иначе возвращаем 0
    return max(0, remaining_days)
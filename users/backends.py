from django.utils import timezone
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

class ExpirationCheckBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        # Рассчитываем дату одного года назад
        one_year_ago = timezone.now() - timezone.timedelta(days=365)
        
        # Если пользователь зарегистрировался более года назад, блокируем вход
        if user.date_joined < one_year_ago:
            raise PermissionDenied("Ваша учетная запись заблокирована, так как истек срок её действия.")
        
        # Проверка пароля
        if user.check_password(password):
            return user
        return None

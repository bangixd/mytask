from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, phone_number, email, password, first_name=None, last_name=None, gender=None, age=None):
        if not username:
            raise ValueError('username required')
        if not phone_number:
            raise ValueError('phone number required')
        if not email:
            raise ValueError('email required')
        user = self.model(username=username, phone_number=phone_number, email=self.normalize_email(email),
                          first_name=first_name, last_name=last_name, age=age, gender=gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, email, password):
        if not username:
            raise ValueError('username required')
        if not phone_number:
            raise ValueError('phone number required')
        if not email:
            raise ValueError('email required')
        user = self.model(username=username, phone_number=phone_number, email=email)
        user.is_superuser = True
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

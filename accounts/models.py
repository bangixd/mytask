from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from model_utils import Choices
from .manager import UserManager

gender_choices = Choices('Male', 'Female', 'either')


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number', ]

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin


# Create your models here.
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.mime import image
from enum import unique
import hashlib

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_superuser(self, email, user_name, full_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, full_name, password, **other_fields)

    def create_user(self, email, user_name, full_name , password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        if not user_name:
            raise ValueError(_('You must provide a username'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          full_name=full_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, user_name, full_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        return self.create_user(email, user_name, full_name , password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    id=models.AutoField(primary_key=True, auto_created=True)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    img= models.ImageField(null=True, upload_to='images/')

    full_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(
        _('last login'), default=timezone.now)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.user_name


class Hashed_code(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=225, unique=True)
    user_email = models.EmailField(max_length=225)

    # hash code on save
    # def save(self, *args, **kwargs):
    #     self.code = Hashed_code.encrypt_password(self.code)
    #     super(Hashed_code, self).save(*args, **kwargs)

    @staticmethod
    def encrypt_password(password):

        return hashlib.sha256(password.encode()).hexdigest()

    # compare the hashed code
    def check_code(user_email, code):
        hashed_code = Hashed_code.objects.get(user_email=user_email)
        e_code = hashed_code.code

        return code == e_code

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Hashed Code"
        verbose_name_plural = "Hashed Codes"
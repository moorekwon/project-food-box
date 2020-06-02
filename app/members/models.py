import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, birth, password=None):
        if not email:
            raise ValueError('email 주소가 필요합니다.')
        if not nickname:
            raise ValueError('nickname이 필요합니다.')
        if not birth:
            raise ValueError('생년월일 정보가 필요합니다.')

        user = self.model(email=self.normalize_email(email), nickname=nickname, birth=birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, birth, password):
        user = self.create_user(email=self.normalize_email(email), nickname=nickname, birth=birth, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER = (
        ('male', '남자'),
        ('female', '여자'),
    )

    email = models.EmailField(max_length=60, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    birth = models.DateField()

    date_created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'birth']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def age(self):
        if self.birth:
            birth_year = str(self.birth).split('-')[0]
            print('birth_year >> ', birth_year)
            return f'{int(birth_year)}대'
        else:
            pass

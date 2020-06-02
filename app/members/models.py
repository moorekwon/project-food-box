import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, birth, gender, password=None):
        if not email:
            raise ValueError('email 주소가 필요합니다.')
        if not nickname:
            raise ValueError('nickname이 필요합니다.')
        if not birth:
            raise ValueError('생년월일 정보가 필요합니다.')
        if not gender:
            raise ValueError('성별 정보가 필요합니다.')

        user = self.model(email=self.normalize_email(email), nickname=nickname, birth=birth, gender=gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, birth, gender, password):
        user = self.create_user(email=self.normalize_email(email), nickname=nickname, birth=birth, gender=gender,
                                password=password)
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
    REQUIRED_FIELDS = ['nickname', 'birth', 'gender', ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def line(self):
        if self.birth:
            today = datetime.date.today()
            today_year = str(today).split('-')[0]
            birth_year = str(self.birth).split('-')[0]
            age = int(today_year) - int(birth_year) + 1
            if 0 < age < 10:
                line = '10대 미만'
            elif 10 <= age < 20:
                line = '10대'
            elif 20 <= age < 30:
                line = '20대'
            elif 30 <= age < 40:
                line = '30대'
            elif 40 <= age < 50:
                line = '40대'
            elif 50 <= age < 60:
                line = '50대'
            elif 60 <= age < 70:
                line = '60대'
            elif 70 <= age:
                line = '70대 이상'
            return line
        else:
            pass

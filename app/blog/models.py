from django.db import models

# 유저 모델
class User(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name

# 유저 정보
class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
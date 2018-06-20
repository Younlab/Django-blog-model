from django.db import models

# 유저 모델
class User(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )

    # 나의 친구 목록을 출력
    def show_friends(self):
        print(self.name,' 의 친구 목록')
        show = self.friends.all()
        for i in show:
            print('-',i)

    def __str__(self):
        return self.name

# 유저 정보
class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='info',
    )

    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.user}\n' \
        f'{self.address}\n' \
        f'{self.phone_number}'

# 글 모델
class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='post',
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}\n' \
               f'{self.user}\n' \
               f'{self.content}\n' \
               f'{self.created_at}' \

# 댓글
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

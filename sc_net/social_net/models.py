from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Announcement(models.Model):
    person = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        default='Новая запись!'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    picture = models.JSONField(
        verbose_name='URL-картинки',
        default=[],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата редактирования'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f'{self.title} ,\n {self.person} | \n {self.created_at}'



class Person(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name='Служебное имя'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Имя профиля',
        null=True,
        blank=True
    )
    age = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Возраст',
        null=True,
        blank=True
    )
    about = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    image = models.JSONField(
        verbose_name='Фотографии',
        default=[
            'https://www.pngkey.com/png/detail/230-2301779_best-classified-apps-default-user-profile.png',
        ],
        null = True,
        blank = True
    )
    friends = models.JSONField(
        verbose_name='Список друзей',
        default=[
            'Nizier193',
        ]
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )



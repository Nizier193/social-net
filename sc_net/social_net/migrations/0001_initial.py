# Generated by Django 4.2 on 2023-07-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=255, verbose_name='Имя')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('picture', models.JSONField(default={}, verbose_name='URL-картинки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Служебное имя')),
                ('name', models.CharField(max_length=255, verbose_name='Имя профиля')),
                ('age', models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Возраст')),
                ('about', models.TextField(default='Пользователь не добавил описание', verbose_name='Описание')),
                ('image', models.JSONField(default={'https://www.pngkey.com/png/detail/230-2301779_best-classified-apps-default-user-profile.png'}, verbose_name='Фотографии')),
                ('friends', models.JSONField(default={'Nizier193'}, verbose_name='Список друзей')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-08-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0004_announcement_user_person_user_alter_person_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=2, default=10, max_digits=10, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.JSONField(blank=True, default=['https://www.pngkey.com/png/detail/230-2301779_best-classified-apps-default-user-profile.png'], null=True, verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя профиля'),
        ),
    ]

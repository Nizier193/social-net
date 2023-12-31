# Generated by Django 4.2 on 2023-08-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0005_alter_person_age_alter_person_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='about',
            field=models.TextField(blank=True, default='Пользователь не добавил описание', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Возраст'),
        ),
    ]

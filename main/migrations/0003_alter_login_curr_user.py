# Generated by Django 4.0 on 2022-10-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='curr_user',
            field=models.CharField(max_length=30),
        ),
    ]

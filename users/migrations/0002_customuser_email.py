# Generated by Django 5.2.1 on 2025-05-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='usuario@telopago.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.7 on 2021-11-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211116_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='randomno',
            field=models.DecimalField(decimal_places=10, default=35.256488115, max_digits=15),
        ),
    ]

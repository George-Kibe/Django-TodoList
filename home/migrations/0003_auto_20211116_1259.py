# Generated by Django 3.1.7 on 2021-11-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211116_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskdesc',
            field=models.TextField(),
        ),
    ]

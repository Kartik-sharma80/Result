# Generated by Django 3.1.2 on 2022-07-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0023_auto_20220707_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]

# Generated by Django 3.1.2 on 2022-07-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0021_auto_20220706_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2022-07-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0011_auto_20220702_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2022-08-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0025_auto_20220708_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2022-07-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0008_auto_20220702_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 3.1.2 on 2022-07-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_auto_20220702_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='result/static/img'),
        ),
    ]

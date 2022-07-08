# Generated by Django 3.1.2 on 2022-07-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('result', '0013_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=20, null=True)),
                ('year', models.CharField(max_length=20, null=True)),
                ('file', models.FileField(default=None, null=True, upload_to='')),
            ],
        ),
    ]
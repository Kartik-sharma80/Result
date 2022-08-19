# Generated by Django 3.1.2 on 2022-06-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('enrollno', models.CharField(max_length=50)),
                ('sub1', models.CharField(max_length=150)),
                ('sub2', models.CharField(max_length=150)),
                ('sub3', models.CharField(max_length=150)),
                ('sub4', models.CharField(max_length=150)),
                ('examname', models.CharField(max_length=150)),
                ('date', models.DateField()),
            ],
        ),
    ]
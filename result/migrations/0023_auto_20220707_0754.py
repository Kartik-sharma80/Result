# Generated by Django 3.1.2 on 2022-07-07 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0022_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
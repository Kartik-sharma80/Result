# Generated by Django 3.1.2 on 2022-08-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0027_auto_20220815_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sub1_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub2_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub3_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub4_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub5_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub6_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub7_marks',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
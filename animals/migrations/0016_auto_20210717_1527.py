# Generated by Django 3.2.5 on 2021-07-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0015_auto_20210717_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='image',
        ),
        migrations.AlterField(
            model_name='animal',
            name='feeding_schedule',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='heating',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='lighting',
            field=models.TextField(),
        ),
    ]

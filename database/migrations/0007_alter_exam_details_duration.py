# Generated by Django 3.2.6 on 2021-11-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20211115_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_details',
            name='duration',
            field=models.DurationField(help_text='(HH:MM:SS)'),
        ),
    ]

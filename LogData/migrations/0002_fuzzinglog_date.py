# Generated by Django 4.0.3 on 2022-05-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuzzinglog',
            name='date',
            field=models.CharField(default=5, max_length=1000),
            preserve_default=False,
        ),
    ]
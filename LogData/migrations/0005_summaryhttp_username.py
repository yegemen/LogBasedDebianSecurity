# Generated by Django 4.0.3 on 2022-06-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogData', '0004_rename_ip_summaryauth_resourceuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='summaryhttp',
            name='username',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
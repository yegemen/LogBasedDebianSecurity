# Generated by Django 4.0.3 on 2022-06-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0005_trycount_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='password',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]

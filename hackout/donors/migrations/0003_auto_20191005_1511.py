# Generated by Django 2.2.4 on 2019-10-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0002_auto_20191004_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='donor',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='donor',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]

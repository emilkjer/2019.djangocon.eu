# Generated by Django 2.1.4 on 2019-03-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretalx_utils', '0003_auto_20190303_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkextraproperties',
            name='announced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talkextraproperties',
            name='workshop',
            field=models.BooleanField(default=False),
        ),
    ]

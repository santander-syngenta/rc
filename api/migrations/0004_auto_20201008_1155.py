# Generated by Django 3.0.8 on 2020-10-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201006_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

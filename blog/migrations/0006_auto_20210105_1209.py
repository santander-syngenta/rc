# Generated by Django 3.1 on 2021-01-05 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_announcement_text2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='text2',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='announcement',
            old_name='text',
            new_name='headline',
        ),
    ]

# Generated by Django 2.0.2 on 2018-07-30 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contenido',
            new_name='content',
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_voter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]

# Generated by Django 5.2 on 2025-05-13 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysteries', '0017_developer_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='contact',
        ),
    ]

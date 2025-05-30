# Generated by Django 5.2 on 2025-05-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysteries', '0007_alter_theory_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theory',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='theory',
            name='image',
            field=models.ImageField(default='default.png', upload_to='theories/'),
        ),
    ]

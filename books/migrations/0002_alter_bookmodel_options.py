# Generated by Django 5.1.5 on 2025-02-15 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'книгу', 'verbose_name_plural': 'книги'},
        ),
    ]

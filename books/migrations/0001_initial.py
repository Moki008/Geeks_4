# Generated by Django 5.1.5 on 2025-02-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Загрузите фото')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название книги')),
                ('description', models.TextField(blank=True, verbose_name='Напишите краткое описание книги')),
                ('price', models.PositiveIntegerField(blank=True, verbose_name='Укажите цену')),
                ('release_date', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('History', 'History'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Fantasy', 'Fantasy')], default='None', max_length=10, verbose_name='Укажите жанр')),
                ('mail_author', models.CharField(default='None', max_length=100, verbose_name='Укажите почту автора')),
                ('author', models.CharField(default='None', max_length=100, verbose_name='Напишите имя автора')),
                ('video', models.URLField(verbose_name='Укажите ссылку из YouTube')),
            ],
        ),
    ]

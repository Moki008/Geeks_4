from django.db import models


class BookModel(models.Model):
    GENRE_CHOICES = (
        ('History', 'History'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Fantasy', 'Fantasy'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Напишите краткое описание книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='Укажите цену', blank=True)
    release_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='None', verbose_name='Укажите жанр')
    mail_author = models.CharField(max_length=100, default='None',verbose_name='Укажите почту автора')
    author = models.CharField(max_length=100, default='None', verbose_name='Напишите имя автора')
    video = models.URLField(verbose_name='Укажите ссылку из YouTube')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'

class Review(models.Model):
    STARS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"),
    )
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,
                                    related_name='book', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    review_text = models.TextField(default='')
    stars = models.CharField(max_length=10, choices=STARS, default='🌟🌟')
    def __str__(self):
        return f'{self.stars}-{self.book.title}'
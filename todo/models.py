from django.db import models
from books.models import BookModel

class TodoModel(models.Model):
    TASK_CHOICES = (
        ('Прочитаю','Прочитаю'),
        ("Прочитал","Прочитал"),
        ("Буду читать","Буду читать")
    )
    task = models.CharField(max_length=100, null=True, blank=True)
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TASK_CHOICES)

    def __str__(self):
        return self.task



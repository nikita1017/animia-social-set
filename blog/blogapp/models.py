from django.db import models

class Anime(models.Model):
    name=models.CharField(max_length=50)
    date=models.CharField(max_length=10)
    author=models.CharField(max_length=25)
    description=models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    genres = (
        ('Аниме', "Аниме"),
        ('Сёнен', "Сёнен"),
        ('Сёнен-ай', "Сёнен-ай"),
        ('Сэнтай', "Сэнтай"),
        ('Сёдзё', "Сёдзё"),
        ('Сэйнэн', "Сэйнэн"),
        ('Дзёсэй', "Дзёсэй"),
        ('Комедия', "Комедия"),
        ('Пародия', "Пародия"),
        ('Романтика', "Романтика"),
        ('Мыльная опера', "Мыльная опера"),
        ('Школьная мыльная опера', "Школьная мыльная опера"),
        ('Гарем', "Гарем"),

    )
    genre = models.CharField(max_length=200, choices=genres)
# Create your models here.

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.IntegerField()

    # Define choices for authors
    AUTHOR_CHOICES = [
        ('JRR Martin', 'JRR Martin'),
        ('Dostoievski', 'Dostoievski'),
        ('Tolken', 'Tolken'),
    ]
    author = models.CharField(max_length=100, choices=AUTHOR_CHOICES)

    # Define choices for categories
    CATEGORY_CHOICES = [
        ('Fantasy', 'Fantasy'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Drama', 'Drama'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    COVER_TYPES = [
        ('hardback', 'Hardback'),
        ('paperback', 'Paperback'),
        ('special', 'Special'),
    ]
    cover_type = models.CharField(max_length=20, choices=COVER_TYPES)

    def __str__(self):
        return self.name

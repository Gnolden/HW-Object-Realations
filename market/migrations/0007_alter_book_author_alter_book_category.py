# Generated by Django 5.0.4 on 2024-04-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(choices=[('JRR Martin', 'JRR Martin'), ('Dostoievski', 'Dostoievski'), ('Tolken', 'Tolken')], max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Fantasy', 'Fantasy'), ('Sci-Fi', 'Sci-Fi'), ('Drama', 'Drama')], max_length=50),
        ),
    ]

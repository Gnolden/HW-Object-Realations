# Generated by Django 5.0.4 on 2024-04-18 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_remove_book_category_alter_book_cover_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.category'),
        ),
    ]

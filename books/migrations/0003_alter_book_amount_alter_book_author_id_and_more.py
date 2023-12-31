# Generated by Django 4.2.3 on 2023-07-27 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_alter_book_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="amount",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="author_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="books.author",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="books.genre",
            ),
        ),
    ]

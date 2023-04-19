# Generated by Django 4.2 on 2023-04-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MainFeed",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        help_text="Заголовок RSS-канала",
                        max_length=512,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "url",
                    models.URLField(help_text="Ссылка на RSS", verbose_name="Ссылка"),
                ),
                (
                    "slug",
                    models.SlugField(help_text="Слаг RSS-канала", verbose_name="Слаг"),
                ),
            ],
            options={
                "verbose_name": "Основной RSS-канал",
                "verbose_name_plural": "Основные RSS-каналы",
            },
        ),
    ]

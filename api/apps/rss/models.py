from django.db import models


class Feed(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=512, verbose_name="Заголовок", help_text="Заголовок RSS-канала"
    )
    url = models.URLField(verbose_name="Ссылка", help_text="Ссылка на RSS")

    class Meta:
        abstract = True


class MainFeed(Feed):
    slug = models.SlugField(
        unique=True, verbose_name="Слаг", help_text="Слаг RSS-канала"
    )

    class Meta:
        verbose_name = "Основной RSS-канал"
        verbose_name_plural = "Основные RSS-каналы"

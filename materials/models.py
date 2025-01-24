from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    image = models.ImageField(upload_to="preview/", blank=True, null=True, verbose_name="Предварительный просмотр")
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lessons(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    image = models.ImageField(
        upload_to="preview/lessons/", blank=True, null=True, verbose_name="Предварительный просмотр"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    link = models.CharField(max_length=10000, blank=True, null=True, verbose_name="Ссылка на видео")
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Курс")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Sign(models.Model):
    name = models.CharField("Имя ребёнка", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    comment = models.TextField("Комментарий", blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.name} — {self.course.name}"

class Review(models.Model):
    author = models.CharField("Имя", max_length=100)
    text = models.TextField("Отзыв")
    rating = models.PositiveSmallIntegerField("Оценка", default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.author}  с оценкой {self.rating}"







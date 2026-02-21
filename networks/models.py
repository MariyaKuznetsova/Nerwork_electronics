from django.db import models


class NetworkNode(models.Model):
    """Класс звено сети"""

    NODE_TYPES = (
        ("factory", "Завод"),
        ("retail", "Розничная сеть"),
        ("IP", "Индивидуальный предприниматель"),
    )
    """Контакты"""
    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Страна"
    )
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    street = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Улица"
    )
    house_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Номер дома"
    )

    """Продукты"""
    name_product = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Модель"
    )
    release_date = models.DateField(
        blank=True, null=True, verbose_name="Дата выхода продукта на рынок"
    )

    type = models.CharField(
        max_length=20,
        choices=NODE_TYPES,
        blank=True,
        null=True,
        verbose_name="Тип звена",
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Поставщик",
    )
    level = models.IntegerField(default=0, editable=False, verbose_name="Уровень сети")

    def save(self, *args, **kwargs):
        """Определение уровня сети"""
        if not self.supplier:
            self.level = 0
        else:
            self.level = self.supplier.level + 1
        super().save(*args, **kwargs)

    debt = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00, verbose_name="Задолженность"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()}) - Уровень {self.level}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
        ordering = [
            "name",
            "email",
            "country",
            "city",
            "name_product",
            "model",
            "debt",
            "created_at",
        ]

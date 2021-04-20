from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(AbstractUser):
    """Модель пользователя"""
    username = models.CharField("Логин", max_length=50, unique=True)
    first_name = models.CharField("Фамилия", max_length=100)
    last_name = models.CharField("Имя", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    position = models.CharField("Должность", max_length=255)

    class Meta:
        verbose_name = 'Пользователь'

    @property
    def fio(self):
        """Возвращает ФИО целиком"""
        return f"{self.first_name} {self.last_name} {self.patronymic}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"


class OrganizationMetod(models.Model):
    """Организации методистов"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)
    href = models.URLField("Ссылка")

    class Meta:
        verbose_name = 'Организации методистов'

    def __str__(self):
        return self.name


STAFF_CHOICES = (
    (0, "Количественный состав"),
    (1, "Постоянные, совместители"),
    (2, "Квалификационный ценз"),
    (3, "Образовательный ценз")
)


class Staff(models.Model):
    """Персонал"""
    type = models.IntegerField("Тип", choices=STAFF_CHOICES)
    name = models.CharField("Название", max_length=255)
    value = models.PositiveIntegerField("Значение")

    class Meta:
        verbose_name = 'Персонал'

    def __str__(self):
        return self.name


class StaffCategory(models.Model):
    """Категории персонала"""
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)
    value = models.PositiveIntegerField("Значение")

    class Meta:
        verbose_name = 'Категории персонала'

    def __str__(self):
        return self.name


class Regulations(models.Model):
    """Нормативно правовые акты"""
    name = models.CharField("Название", max_length=255)
    file = models.FileField("Файл", upload_to='regulations/')

    class Meta:
        verbose_name = 'Нормативно правовые акты'


class District(models.Model):
    """Районы"""
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = 'Районы'

    def __str__(self):
        return self.name


class Udo(models.Model):
    """Учреждения дошкольного образования"""
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)
    href = models.URLField("Ссылка")

    class Meta:
        verbose_name = 'Учреждения дошкольного образования'

    def __str__(self):
        return self.name




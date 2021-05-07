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
        verbose_name_plural = 'Пользователь'

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
        verbose_name_plural = 'Организации методистов'

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
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return self.name


class StaffCategory(models.Model):
    """Категории персонала"""
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)
    value = models.PositiveIntegerField("Значение")

    class Meta:
        verbose_name = 'Категории персонала'
        verbose_name_plural = 'Категории персонала'

    def __str__(self):
        return self.name


class Regulations(models.Model):
    """Нормативно правовые акты"""
    name = models.CharField("Название", max_length=255)
    file = models.FileField("Файл", upload_to='regulations/')

    class Meta:
        verbose_name = 'Нормативно правовые акты'
        verbose_name_plural = 'Нормативно правовые акты'

    def __str__(self):
        return self.name


class District(models.Model):
    """Районы"""
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = 'Районы'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class Udo(models.Model):
    """Учреждения дошкольного образования"""
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)
    href = models.URLField("Ссылка")

    class Meta:
        verbose_name = 'Учреждения дошкольного образования'
        verbose_name_plural = 'Учреждения дошкольного образования'

    def __str__(self):
        return self.name


UNION_INTERES_CHOICES_TYPE = (
    (0, "Всего"),
    (1, "В сельской местности"),
    (2, "По профилям деятельности")
)

# UNION_INTERES_CHOICES_PROFILE = (
#     (0, ""),
#     (1, "")
# )


class UnionInteres(models.Model):
    """Объединения по интересам"""
    type = models.IntegerField("Тип", choices=UNION_INTERES_CHOICES_TYPE)
    # profile = models.IntegerField("Профиль", choices=STAFF_CHOICES)
    profile = models.ForeignKey('UnionInteresProfile', verbose_name="Профиль", on_delete=models.CASCADE, null=True,
                                blank=True)
    group_value = models.PositiveIntegerField("Количество групп")
    people_value = models.PositiveIntegerField("Количество людей")

    class Meta:
        verbose_name = 'Объединения по интересам'
        verbose_name_plural = 'Объединения по интересам'

    def __str__(self):
        return self.get_type_display()


class UnionInteresProfile(models.Model):
    """Профили для объединений по интересам"""
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Профили для объединений по интересам'
        verbose_name_plural = 'Профили для объединений по интересам'

    def __str__(self):
        return self.name

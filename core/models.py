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
    staff = models.ForeignKey(Staff, verbose_name="Персонал", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)
    value = models.PositiveIntegerField("Значение", null=True, blank=True)

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


DISTRICT_CHOICE = (
    (1, 'Житковичский район'),
    (2, 'Петриковский район'),
    (3, 'Октябрьский район'),
    (4, 'Светлогорский район'),
    (5, 'Жлобинский район'),
    (6, 'Рогачевский район'),
    (7, 'Кормянский район'),
    (8, 'Чечерский район'),
    (9, 'Ветковский район'),
    (10, 'Буда-Кошелёвский район'),
    (11, 'Добрушский район'),
    (12, 'Гомельский район'),
    (13, 'Речицкий район'),
    (14, 'Лоевский район'),
    (15, 'Брагинский район'),
    (16, 'Хойникский район'),
    (17, 'Калинковичский район'),
    (18, 'Наровлянский район'),
    (19, 'Мозырский район'),
    (20, 'Ельский район'),
    (21, 'Лельчицкий район'),
    (22, 'г. Гомель'),
)


class Udo(models.Model):
    """Учреждения дошкольного образования"""
    district = models.IntegerField("Район", choices=DISTRICT_CHOICE)
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


class UnionInteres(models.Model):
    """Объединения по интересам"""
    type = models.IntegerField("Тип", choices=UNION_INTERES_CHOICES_TYPE)
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


class MetodicEvent(models.Model):
    """Методические мероприятия(вместо инновационной деятельности)"""
    name = models.CharField("Название", max_length=255)
    file = models.FileField("Файл", upload_to='metodic_events/')

    class Meta:
        verbose_name = 'Методические мероприятия'
        verbose_name_plural = 'Методические мероприятия'

    def __str__(self):
        return self.name

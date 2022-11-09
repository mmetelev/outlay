from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings

from ..base.genrate_path import generate_user_file_path


class SN(models.Model):
    """Стоимостные нормативы"""
    cipher = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    quantity = models.IntegerField()
    spgz_name = models.CharField(max_length=150)
    id = models.IntegerField(primary_key=True)
    kpzg = models.CharField(max_length=150)
    unit2 = models.CharField(max_length=150)
    quantity2 = models.IntegerField()


class TSN(models.Model):
    """Территориальные сметные нормативы"""
    cipher = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    quantity = models.IntegerField()
    spgz_name = models.CharField(max_length=150)
    id = models.IntegerField(primary_key=True)
    kpzg = models.CharField(max_length=150)
    unit2 = models.CharField(max_length=150)
    quantity2 = models.IntegerField()


class SPGZFile(models.Model):
    """
    Справочник предметов государственного заказа,
    импорт данных из excel файла
    """
    file = models.FileField(
        upload_to=generate_user_file_path,
        validators=[FileExtensionValidator(allowed_extensions=["xlsx", "xls"])],
        blank=True,
        null=True
    )


class SPGZ(models.Model):
    """Справочник предметов государственного заказа"""
    id = models.IntegerField(primary_key=True)
    kpzg = models.TextField()
    spgz_name = models.CharField(max_length=300)
    unit = models.CharField(max_length=50)
    okpd = models.CharField(max_length=50)
    okpd2 = models.CharField(max_length=50)


class SNFile(models.Model):
    """
    Стоимостные нормативы, обновление справочника
    """
    file = models.FileField(
        upload_to=generate_user_file_path,
        validators=[FileExtensionValidator(allowed_extensions=["xlsx", "xls"])],
        blank=True,
        null=True
    )


class TSNFile(models.Model):
    """
    Территориальные сметные нормативы, обновление справочника
    """
    file = models.FileField(
        upload_to=generate_user_file_path,
        validators=[FileExtensionValidator(allowed_extensions=["xlsx", "xls"])],
        blank=True,
        null=True
    )


class Template(models.Model):
    """Шаблон сметы"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    kpzg = models.CharField(max_length=150)
    name_spgz = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TemplateFile(models.Model):
    """Файл обновления шаблонов сметы"""
    file = models.FileField(
        upload_to=generate_user_file_path,
        validators=[FileExtensionValidator(allowed_extensions=["xlsx", "xls"])],
        blank=True,
        null=True
    )


class Estimate(models.Model):
    """Смета пользователя"""
    TYPE = (
        ('tz', 'ТЗ'),
        ('spgz', 'СПГЗ')
    )
    file = models.FileField(
        upload_to=generate_user_file_path,
        validators=[FileExtensionValidator(allowed_extensions=["xlsx", "xls"])]
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE)
    sample = models.ForeignKey(Template, on_delete=models.CASCADE, blank=True)
    spgz = models.ManyToManyField(SPGZ, blank=True)
    address = models.CharField(max_length=100, blank=True)
    is_address = models.BooleanField(default=True)
    price_list = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Author id: {self.author_id}, file id: {self.id}'


class ResultFile(models.Model):
    """Файл с результатом выполнения"""
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    kpgz = models.IntegerField()
    work_code = models.IntegerField()
    name_of_works = models.TextField(max_length=500)
    unit_of_measurement = models.CharField(max_length=50)
    spgz = models.IntegerField()
    quantity = models.IntegerField()
    unit_price_tru = models.DecimalField(decimal_places=2, max_digits=10)
    price_tru = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Result estimate {self.estimate_id}'

from . import models

from rest_framework import serializers


class EstimateSerializer(serializers.ModelSerializer):
    """Файл пользователя"""

    class Meta:
        model = models.Estimate
        fields = ('id', 'file', 'author', 'sample', 'address', 'type', 'is_address', 'price_list', 'created')


class EstimateListSerializer(serializers.ModelSerializer):
    """Список файлов пользователя"""

    class Meta:
        model = models.Estimate
        fields = '__all__'


class EstimateCreateSerializer(serializers.ModelSerializer):
    """Создание файла"""

    class Meta:
        model = models.Estimate
        fields = '__all__'


class SPGZSerializer(serializers.ModelSerializer):
    """Справочник предметов государственного заказа"""

    class Meta:
        model = models.SPGZ
        fields = '__all__'


class SPGZExcelSerializer(serializers.ModelSerializer):
    """
    Справочник предметов государственного заказа,
    импорт данных из excel файла
    """

    class Meta:
        model = models.SPGZFile
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):
    """Справочник предметов государственного заказа"""

    class Meta:
        model = models.Template
        fields = '__all__'


class TemplateFileSerializer(serializers.ModelSerializer):
    """Файл для обновления справочника шаблонов"""

    class Meta:
        model = models.TemplateFile
        fields = '__all__'


class SNSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SN
        fields = '__all__'


class TSNSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TSN
        fields = '__all__'


class TSNFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TSNFile
        fields = "__all__"


class SNFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SNFile
        fields = "__all__"

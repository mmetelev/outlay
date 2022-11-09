from rest_framework import parsers, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers, services

from ..base.classes import MixedSerializer
from ..base.permissions import IsAuthor, IsModerator, IsAdministrator


class EstimateView(MixedSerializer, ModelViewSet):
    """Смета пользователя"""
    serializer_classes_by_action = {
        'list': serializers.EstimateListSerializer,
        'create': serializers.EstimateCreateSerializer,
        'update': serializers.EstimateSerializer,
        'destroy': serializers.EstimateSerializer,
        'retrieve': serializers.EstimateSerializer
    }
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAdministrator | IsModerator | IsAuthor]

    def get_queryset(self):
        return (
            models.Estimate.objects.filter(author=self.request.user)
            .select_related("author")
            .all()
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        serialized = serializers.SPGZExcelSerializer(data=request.data)
        if serialized.is_valid():
            file = request.data['file']
            services.upload_file(file)
            return Response(status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class SNView(ModelViewSet):
    queryset = models.SN.objects.all()
    serializer_class = serializers.SNSerializer


class TSNView(ModelViewSet):
    queryset = models.TSN.objects.all()
    serializer_class = serializers.TSNSerializer


class SPGZView(ModelViewSet):
    """Справочник предметов государственного заказа"""
    parser_classes = (parsers.MultiPartParser,)
    queryset = models.SPGZ.objects.all()
    serializer_class = serializers.SPGZSerializer
    permission_classes = [IsAdministrator | IsModerator]


class TemplateView(ModelViewSet):
    """Шаблон сметы"""
    queryset = models.Template.objects.all()
    serializer_class = serializers.TemplateSerializer
    permission_classes = [IsAdministrator | IsModerator]


class TemplateFileView(ModelViewSet):
    """Обновление шаблона, только для администратора"""
    permission_classes = (IsAdministrator,)
    queryset = models.TemplateFile.objects.all()
    serializer_class = serializers.TemplateFileSerializer
    pagination_class = (parsers.MultiPartParser,)

    def create(self, request, *args, **kwargs):
        serialized = serializers.SPGZExcelSerializer(data=request.data)
        if serialized.is_valid():
            file = request.data['file']
            services.import_template_data_from_excel(file)
            return Response(status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class SPGZFileView(ModelViewSet):
    """
    Справочник предметов государственного заказа,
    импорт данных
    """
    parser_classes = (parsers.MultiPartParser,)
    queryset = models.SPGZFile.objects.all()
    serializer_class = serializers.SPGZExcelSerializer
    permission_classes = [IsAdministrator | IsModerator]

    def create(self, request, *args, **kwargs):
        serialized = serializers.SPGZExcelSerializer(data=request.data)
        if serialized.is_valid():
            file = request.data['file']
            services.import_spgz_data_from_excel(file)
            return Response(status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class TSNFileView(ModelViewSet):
    """
    Территориальные сметные нормативы, импорт данных из файла,
    только для администратора
    """
    permission_classes = (IsAdministrator,)
    queryset = models.TSNFile.objects.all()
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.TSNFileSerializer

    def create(self, request, *args, **kwargs):
        serialized = serializers.SPGZExcelSerializer(data=request.data)
        if serialized.is_valid():
            file = request.data['file']
            services.import_tcn_data_from_excel(file)
            return Response(status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class SNFileView(ModelViewSet):
    """
    Стоимостные нормативы, обновление справочника,
    только дял администратора
    """
    permission_classes = (IsAdministrator,)
    queryset = models.SNFile.objects.all()
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.SNFileSerializer

    def create(self, request, *args, **kwargs):
        serialized = serializers.SPGZExcelSerializer(data=request.data)
        if serialized.is_valid():
            file = request.data['file']
            services.import_sn_data_from_excel(file)
            return Response(status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

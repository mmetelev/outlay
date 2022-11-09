from django.urls import path

from . import views

urlpatterns = [

    # Справочники
    path('sn/', views.SNView.as_view({"get": "list"})),
    path('tsn/', views.TSNView.as_view({"get": "list"})),
    path('spgz/', views.SPGZView.as_view({"get": "list"})),

    # Смета от пользователя
    path('estimates/', views.EstimateView.as_view({"post": "create", "get": "list"})),
    path('estimates/<int:pk>/', views.EstimateView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),

    # Шаблон сметы
    path('template/', views.TemplateView.as_view({"get": "list"})),
    path('template/<int:pk>/', views.TemplateView.as_view({"get": "retrieve"})),

    # Обновление справочников
    path('create-spgz/', views.SPGZFileView.as_view({"post": "create"})),
    path('create-sn/', views.SNFileView.as_view({"post": "create"})),
    path('create-tsn/', views.TSNFileView.as_view({"post": "create"})),
    path('create-template/', views.TemplateView.as_view({"post": "create"}))
]

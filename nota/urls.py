from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('novo_gasto/', views.add_note, name='novo_gasto'),
    path('info_gasto/<int:pk>', views.detail_gasto, name='info_gasto'),
]
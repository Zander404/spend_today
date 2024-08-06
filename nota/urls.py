from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('novo_gasto/', views.add_note, name='novo_gasto'),
    path('info_gasto/<int:pk>', views.detail_gasto, name='info_gasto'),
    path('update_gasto/<int:pk>', views.update_gasto, name='update_gasto'),
    path('delete_gasto/<int:pk>', views.delete_gasto, name='delete_gasto'),
]
from django.urls import path
from . import views

app_name  = 'transactionalFunction'

urlpatterns = [
    path('', views.TransactionalFuncionList.as_view(), name='list'),
    path('create/', views.TransactionalFuncionCreate.as_view(), name='create'),
    path('show/<int:pk>', views.TransactionalFuncionShow.as_view(), name='show'),
]

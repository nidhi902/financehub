from django.urls import path
from . import views
from .views import FinanceDataView

urlpatterns = [
    # path('', views.index),
    # urls.py

    path('finance/', FinanceDataView.as_view()),
    path('finance/<int:pk>/', FinanceDataView.as_view()),

]
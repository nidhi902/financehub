from django.urls import path
from . import views
from .views import DashboardView, FinanceDataView

urlpatterns = [
    # path('', views.index),
    

    path('finance/', FinanceDataView.as_view()),
    path('finance/<int:pk>/', FinanceDataView.as_view()),
    path('dashboard/', DashboardView.as_view()),

]
from django.urls import path
from tools.views import CalculatorView, PrankCalculatorView, SimpleCalculatorView

urlpatterns = [
    path('calculator', CalculatorView.as_view(), name='calculator'),
    path('prank-calculator', PrankCalculatorView.as_view(), name='prank-calculator'),
    path('simple-calculator', SimpleCalculatorView.as_view(), name='simple-calculator'),
]
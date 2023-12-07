from django.shortcuts import render
from django.views import View

from tools.utils import Calculate
from tools.forms import CalculatorForm

# Create your views here.
class CalculatorView(View):
    def get(self, request):
        form = CalculatorForm()
        context = { 'form': form, 'result': '' }
        return render(request, 'calculator.html', context)
    
    def post(self, request):
        form = CalculatorForm(request.POST)
        if form.is_valid():
            operation = request.POST.get('operation')
            num_1 = form.cleaned_data['num_1']
            num_2 = form.cleaned_data['num_2']

            result = Calculate(num_1, num_2, operation)
            result = 'Nan' if result == None else result
            context = { 'form': form, 'result': result }
            return render(request, 'calculator.html', context)
        else:
            context = { 'form': form, 'result': '' }
            return render(request, 'calculator.html', context)


class PrankCalculatorView(View):
    def get(self, request):
        form = CalculatorForm()
        context = { 'form': form, 'result': '' }
        return render(request, 'prank-calculator.html', context)
    
    def post(self, request):
        form = CalculatorForm(request.POST)
        if form.is_valid():
            operation = request.POST.get('operation')
            num_1 = form.cleaned_data['num_1']
            num_2 = form.cleaned_data['num_2']

            if operation == 'add':
                num_1 = str(num_1)
                num_2 = str(num_2)
            elif operation == 'multiply':
                num_1 = str(num_1)
            elif operation == 'divide':
                num_1 = str(num_1)
                num_1 = [num_1[int(round(len(num_1)/num_2*i)):int(round(len(num_1)/num_2*(i+1)))] for i in range(num_2)]
                num_2 = 1
                operation = 'multiply'

            result = Calculate(num_1, num_2, operation)
            result = 'Nan' if result == None else result
            context = { 'form': form, 'result': result }
            return render(request, 'prank-calculator.html', context)
        else:
            context = { 'form': form, 'result': '' }
            return render(request, 'prank-calculator.html', context)
        

class SimpleCalculatorView(View):
    def get(self, request):
        context = {'form': None}
        return render(request, 'simple-calculator.html', context)
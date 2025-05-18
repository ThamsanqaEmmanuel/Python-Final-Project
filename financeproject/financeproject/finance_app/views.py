from django.shortcuts import render, redirect
from .models import Expense
from finance_app.forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total_expense = sum(exp.amount for exp in expenses)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'finance_app/expense_list.html', {'expenses': expenses, 'form': form, 'total_expense': total_expense})

import reportes;

# Generar reportes de ventas y gastos usando funciones del módulo
sales_report = reportes.generate_sales_report('Octobre', 10000)
expense_report = reportes.generate_expenses_report('Octubre', 5000)

print(sales_report)
print(expense_report)
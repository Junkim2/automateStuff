import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

produceNames = {'garlic': 3.09, 'Celery': 1.19, 'Lemon': 1.25}
list_produceNames = list(produceNames)
print(produceNames.get('garlic'))
for k in range(0, len(list_produceNames)):
    for i in range(1, sheet.max_row+1):
        if list_produceNames[k] == sheet['A'+str(i)].value:
            sheet['B'+str(i)].value = produceNames.get(str(k))
wb.save('new_produceSales.xlsx')
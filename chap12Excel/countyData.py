import openpyxl, pprint

print("loading workbook")
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}
print("reading rows")
for row in range(2, sheet.max_row):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tract':0, 'pop':0})
    countyData[state][county]['tract'] += 1
    countyData[state][county]['pop'] += int(pop)
fileData = open('census2010.py', 'w')
fileData.write('allData = '+ pprint.pformat(countyData))
fileData.close()


import xlwt
import json

file=xlwt.Workbook(encoding='utf-8')
table=file.add_sheet('number',cell_overwrite_ok=True)
txt=open('number.txt').read()
json_txt=json.loads(txt)
for x in range(len(json_txt)):
    for y in range(len(json_txt[x])):
        table.write(x,y,json_txt[x][y])

file.save('number.xls')
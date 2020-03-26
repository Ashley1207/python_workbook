import xlwt
import json
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
#x新建一个excel文件
file=xlwt.Workbook(encoding='utf-8')
#新建一个sheet
table=file.add_sheet('student',cell_overwrite_ok=True)
txt=open('student.txt').read()
print(type(txt))#字符串

json_txt=json.loads(txt)#将json格式数据转化为字典
for x in range(len(json_txt)):
    table.write(x,0,x+1)#写入数据，行，列，数据
    for y in range(len(json_txt[str(x+1)])):
        table.write(x,y+1,json_txt[str(x+1)][y])

file.save('student.xls')
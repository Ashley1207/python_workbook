#统计代码行数
import os
#返回脚本的路径
CODE_PATH=os.path.join(os.path.dirname(__file__),'/Users/ashley/PycharmProjects/workBook/tongji4')
print(CODE_PATH)
code_files=[]
code_line_number=0
code_blank_line_number=0
code_comment_line_number=0

def walk(rootDir):
    global code_files
    for lists in os.listdir(rootDir):
        path=os.path.join(rootDir,lists)
        if os.path.isdir(path):
            walk(path)
        else:
            #分离文件名和扩展名，默认返回(fname,fextension)元组，可做分片操作
            if os.path.splitext(lists)[1].upper()=='.PY':#py要大写
                code_files.append(path)


walk(CODE_PATH)
for code_file in code_files:
    file=open(code_file)
    for line in file:
        code_line_number+=1
        if line=='\n':
            code_blank_line_number+=1
        if line.replace(' ','').replace('\t','')[0]=='#':
            code_comment_line_number+=1

print('文件数量',len(code_files))
print('代码行数',code_line_number)
print('空行行数',code_blank_line_number)
print('注释行数',code_comment_line_number)
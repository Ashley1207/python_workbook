import io
import operator

def get_count_table(file='0004.txt',ignore=[],lower=True):
    txt=open(file).read()
    for i in ignore:
        txt=txt.replace(i,'')
    if lower:
        txt=txt.lower()
    print(txt)
    #str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
    words=txt.split(' ')#变成列表,遇到空忽略
    print(words)
    dec={}
    for word in words:
        if word is '':
            continue
        if word in dec:
            dec[word]+=1
        else:
            dec[word]=1
    return dec

result=sorted(
    get_count_table().items(),key=operator.itemgetter(1),reverse=True
)

for item in result:
    print(item[0])
    print(item[1])
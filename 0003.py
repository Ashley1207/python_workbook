import redis
import uuid

redis_server=redis.StrictRedis(host='localhost',port=6379,db=0)
def create_code(number=200):
    result=[]
    while True is True:
        temp=str(uuid.uuid1()).replace('-','')
        if not temp in result:
            result.append(temp)
        if len(result) is number:
            break
    return result

def clearnUp(prefix='showmethecode'):
    keys=redis_server.keys('%s_*'%prefix)
    for key in keys:
        redis_server.delete(key)

def insertCode(code,prefix='showmethecode'):
    redis_server.set('%s_%s'%(prefix,code),code)

def selectCode(prefix='shoemethecode'):
    keys=redis_server.keys('%s_*'%prefix)
    result=[]
    for key in keys:
        result.append(redis_server.get(key))
    return result

def Process():
    clearnUp()
    code=create_code()
    for c in code:
        insertCode()
    result=selectCode()
    return result

Process()
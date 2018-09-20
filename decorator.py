import time

def decorator(func):
    #kw key word
    def warpper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return warpper


@decorator
def f1(func_name):
    print('This is a function named' + func_name)

@decorator
def f2(func_name1,func_name2):
    print('This is a function named' + func_name1)
    print('This is a function named' + func_name2)
    
@decorator
def f3(func_name1,func_name2,**kw):
    print('This is a function named' + func_name1)
    print('This is a function named' + func_name2)
    print(kw)

f3('test func1','test func2',a=1,b=2,c='123')

f1('test func')
f2('test func1','func2')

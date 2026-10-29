def my_func_decor(func):
def wrapper(x,y):
    if y>x:
        x,y =y,x
        print("values,swapped")
    func()
    print("process completed")


def OriginalFun(x,y):
    def wrapper(x,y)
       
    if x>y:
        f(x/y)
    else:
        x,y = y,x
        print (x,y)

OriginalFun(5,10)

    
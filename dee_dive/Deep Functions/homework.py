
def my_devi_decor(func):
    def wrapper(x,y):
        if isinstance (x,str):
             x = int(x)
        if isinstance (y,str):
            y= int(y)
        func(x,y)
        print("process complted")
    return wrapper

    @my_devi_decor
    def originalfun(x,y):
        print(x,y)
        originalfun('5',10)







#create decorator
#check datatype
#if the values is in string convert int/float
#then follow the rest
def outter2(fp):
    def wrapper():
        print("Flower")
        fp()
    return wrapper

def outter(fp):
    def wrapper():
        print(fp.__name__, "start")
        fp()
        print(fp.__name__, 'end')
    return wrapper

def view_1():
    print('start')
    print('view_1')
    print('end')

@outter2
@outter
def view_2():
    print('view_2')

if __name__ == '__main__':
    view_1()
    # call_1 = outter(view_2)
    # call_1()
    view_2()
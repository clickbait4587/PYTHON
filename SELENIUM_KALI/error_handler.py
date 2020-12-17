import sys
def error_hander(list):
    for i in list:
        try: i
        except:
            e = sys.exc_info()
            print(e)

def one():
    print("One")
def two():
    print("two")
def three():
    rint("three")

error_hander([one(), two()])
try: three()
except:
    e = sys.exc_info()
    print(e)
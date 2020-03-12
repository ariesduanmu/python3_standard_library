# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 09:48:58
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 10:01:54

class MyObject:
    CLASS_ATTRIBUTE = 'some value'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'MyObject({})'.format(self.name)

def f(*args):
    nargs = len(args)
    print(nargs, args)

if __name__ == '__main__':
    from dis import dis
    from dis import show_code
    print("***dis function(f)***")
    dis(f)
    print('-'*25)
    print("***dis function(f) show code***")
    show_code(f)
    print('-'*25)
    print("***dis class(MyObject)***")
    dis(MyObject)
    print('-'*25)
    print("***show code***")
    code = """
my_dict = {'a':1}
    """
    show_code(code)


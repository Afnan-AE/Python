#local -> enclosed -> global -> builtin
#LEBG

#local

def f1():
    x = 1
    print(x)

def f2():
    x = 2
    print(x)

#enclosed

def f3():
    x = 3
    def f31():
        print(x)
    f31()

#Global

x = 4
def f4():
    print(x)

#built in

from math import pi
def f5():
    print(pi)

f1()
f2()
f3()
f4()
f5()
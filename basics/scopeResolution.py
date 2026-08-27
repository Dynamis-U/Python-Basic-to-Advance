#variable scope = where a variable is visible and accessible
#scope resolution = (LEGB) -> Local -> Enclosed -> Global -> Built-in

from math import e # Built-in scope

def func1():
    e = 1  # Local scope
    print(e)

e = 2   # Global scope

def func2():
    e = 3
    func3(e)

def func3(x):   # enclosing scope
    print(x)

func2()

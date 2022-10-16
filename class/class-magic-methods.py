"""
In Python the __new__() magic method is implicitly called before the __init__() method.
The __new__() method returns a new object, which is then initialized by __init__().
"""
class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print ("__init__ magic method is called")
        self.name = "Rahul"


emp = Employee()
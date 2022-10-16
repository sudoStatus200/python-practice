class MyClass:
    def method(self):
        print("I am object method, I can modify class and objects state")

    @classmethod
    def class_method(cls):
        print("I am class method , I can only modify class only")


    @staticmethod
    def static_method():
        print("Neither can modify class nor object")
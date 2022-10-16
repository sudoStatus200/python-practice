"""
This is to demonstrate the working of class attribute
"""
class MyClass(object):
    #These are class attributes which can be accessed from all instances
    class_attr = "I am class"
    mutable_attr = []
    count = 0

    def __init__(self):
        MyClass.count +=1




a = MyClass()
b = MyClass()
#print class attribute from instance, value will be same
print(a.class_attr)
print(a.mutable_attr)

# upadate class attr from instance
a.class_attr = "Updated using instance"

# updated value will be printed, in this case class attr gets turn into instance attributed and gets overriden for instance a only
print(a.class_attr)

#below will still print original class attributed not updated one
print(b.class_attr)



# delete class attr from instance
# this will delete overriden value only
del a.class_attr

# as overridden value is deleted , lookup will go one level above and will print value from class
print(a.class_attr)


# updating a mutable class attr from instance attr
# due to array being referenced , updating from one instance alone will make it change for all instance
a.mutable_attr.append(1)


# both will print same
print(a.mutable_attr)
print(b.mutable_attr)




# below will print class attr from class
print(MyClass.count)


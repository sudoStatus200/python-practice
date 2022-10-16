"""
decorators wrapes up the fucntion/class with decorator function/class
"""


def honirific(cls):
    class HonirificCls(cls):
        def full_name(self):
            return "Mr." + super(HonirificCls, self).full_name()

    return HonirificCls



@honirific
class Name(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


result = Name("Rahul", "Mawari").full_name()
print("Full name: {0}".format(result))

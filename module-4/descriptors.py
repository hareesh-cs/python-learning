class A:
    __secret_value = 1


instance_a = A()
print(instance_a)
# print(instance_a.__secret_value)
print(dir(instance_a))
print(instance_a._A__secret_value)
print(A._A__secret_value)


class B(A):
    pass


instance_b = B()
print(instance_b)
print(dir(instance_b))


class DescriptorClass:
    def __init__(self, intial_value=None, name='var'):
        self.val = intial_value
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving ", self.name)
        return self.val

    def __set__(self, obj, val):
        print("Setting ", self.name)
        self.val = val


class SimpleClass:
    x = DescriptorClass(1, 'x')
    y = 2


s = SimpleClass()
print(s.x)
print(s.y)
s.x=3
print(s.x)
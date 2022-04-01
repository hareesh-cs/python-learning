import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)

    def set_age(self, age):
        self.age = age


# p1=Person('Hareesh',22)
# p1.print_info()
# p1.set_age(25)
# p1.print_info()
#
# with open('hareesh.pickle','wb') as f:
#     pickle.dump(p1,f)

with open('hareesh.pickle', 'rb') as f:
    p1 = pickle.load(f)
p1.print_info()

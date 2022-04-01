import json
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)

    def get_older(self, years):
        self.age += years
    def save_to_json(self,filename):
        person_dict={
            'name': self.name,
            'age': self.age
        }
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict,indent=4))

p1=Person("Michael",31)
p1.print_info()
p1.get_older(3)
p1.save_to_json("Michael.json")
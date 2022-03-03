import json


class Person:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def print_info(self):
        print(self.name, self.age, self.nationality)

    def save_to_json(self, filename):
        person_dict = {'name': self.name, 'age': self.age, 'nationality': self.nationality}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())

        self.name = data['name']
        self.age = data['age']
        self.nationality = data['nationality']


# p1 = Person('Mike', 30, 'English')
# p1 .print_info()
# p1.save_to_json("mike.json")

p2 = Person(None, None, None)
p2.load_from_json("mike.json")
p2.print_info()



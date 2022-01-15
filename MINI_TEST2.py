import self as self


class Person:
    "This is a person class"

    # Static
    # age = 10
    # name= 'out'

    # Can be change
    def __init__(self, age=10, name='idan default'):
        self.age = age
        self.name = name


    def a_func(self):
        name = self.name

        print(f'Hello {name}')

        def b_func():
            print(f'Hello!')
        b_func()


a_person = Person(age=5, name='bob')

# Output: 10
print(a_person.age)

# Output: <function Person.greet>
Person.a_func(a_person)

# Output: "This is a person class"
print(Person.__doc__)


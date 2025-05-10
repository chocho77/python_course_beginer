# snake_case
# PascalCase
# camelCase

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


# Example usage

p = Person("John", "Doe")

print(p.first_name)

p.first_name = "Jane"

print(p.first_name)

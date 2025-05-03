"Hello".isalpha()        # True
"Bonjour".isalpha()      # True
"Hello123".isalpha()     # False (contains numbers)
"Hi there".isalpha()     # False (contains a space)
"".isalpha()             # False (empty string)
"çüéâäà".isalpha()        # True (Unicode alphabetic characters)


def validate_name(name):
    if not name:
        return "Name cannot be empty."
    elif not name.isalpha():
        return "Name must contain only alphabetic characters."
    else:
        return "Name is valid!"

names = ["Alice", "Bob123", "John Doe", "Élodie", ""]


for name in names:
    print(f"{name!r}: {validate_name(name)}")

import datetime


first_name = "John"  # snake case
FirstName = "John"   # Pascal case
firstName = "John"   # Camel case

# 1value - forbidden name
# value*2 - forbidden name

x = 8 # Integer
print(type(x)) # <class 'int'>
pi = 3.141592 # Real number
print(type(pi)) # <class 'float'>
overflow = 3.1234567891011121314
print(overflow)
is_user_logged_in = True # Boolean
print(is_user_logged_in)
comment = "Hello" # str
print(comment)
current_date_time = datetime.datetime.now()
print(current_date_time)
print(1, 2, 3) # prints multiple values
print(1, 2, 3, sep="-") # print with a separator
print(1, 2, 3, sep="!")
print(1, 2, 3, end="!!!!!") # print with  an end
print(1, 2, 3, end="!!!!!\n")
print("Done")
print(1, 2 ,3, sep="\"some text\"", end="\n") # print with both
x = 123456789011111123456789011111 # Long integer
y = 123456789011111123456789011111 # Long integer
print(f"x = {x}")
print(f"y = {y}")
print(f"x + y = {x+y}") # add long integer
print(f"x * y = {x * y}") # multiply long integer
text = "\"Hello\""
print(text) # Escape
tab = "\t" # use tab
print(f"{tab} {text}") # tab
text = '"Hello\n\n\n"'
print(text)
text = '"Hello\n\n\n\t"'
print(text)
result_add_numbers = 3 + 4
print(result_add_numbers)
result_sub_numbers = 5 - 4
print(result_sub_numbers)
result_multy_numbers = 4 * 3
print(result_multy_numbers)
result_divide_numbers = 4 / 3 # Float division
print(result_divide_numbers)
result_whole_divide_numbers = 4 // 3 # Integer division
print(result_whole_divide_numbers)
x = 6
y = 8
result_pow = x ** y
print(f"{x} ** {y} = {result_pow}")

print(5 % 3) # division with remain : remain is 2



















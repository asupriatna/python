import this

print()
new_string = "This is a String"  # storing a string
print('ID:', id(new_string))  # shows the object identifier (address)
print('Type:', type(new_string))  # shows the object type
print('Value:', new_string)  # shows the object value

print()
print(">>concate string")
simple_string = 'Hello!' + " I'm a simple string"
print(simple_string)

#multi-line string, note the \n (newline) escape character automatically created

multi_line_string = """Hello I'm
a multi-line
string!"""
print()
print(">>multi-line string")
print(multi_line_string)


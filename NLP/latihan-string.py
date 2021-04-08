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

# unicode string literals
string_with_unicode = 'H\u00e8llo!'
print()
print(">>unicode string literals")
print(string_with_unicode)


s2 = '-- Python --'
print()
print(">>more concate string 1")
print(s2 * 5)

print()
print(">>more concate string 2")
s3 = ('This '
      'is another way '
      'to concatenate '
      'several strings!')
print(s3)

s= "PYTHON"
# depicting string indexes
for index, character in enumerate(s):
    print('Character ->', character, 'has index->', index)


#String slicing
print()
print(">>String slicing")
print('s[:] = ',s[:])
print('s[1:4] = ',s[1:4])
print('s[:3], s[3:] = ',s[:3], s[3:])
print('s[-3:] = ',s[-3:])
print('s[:3] + s[3:] =',s[:3] + s[3:])

#Case conversions
print()
print(">>Case conversions")
s = 'python is great'
print('s.capitalize() =',s.capitalize())
print('s.upper() = ',s.upper())
print('s.title() = ',s.title())

print('replace(\'python\', \'NLP\') = ',s.replace('python', 'NLP'))


#Case conversions
print()
print(">> splitting and joining")
#String splitting and joining
s = 'I,am,a,comma,separated,string'
print(s.split(','))

s = ' '.join(s.split(','))
print("\n>> Join\n",s)

#Formatting strings using the format method
s='Hello {} {}, it is a great {} to meet you at {}'
txt = s.format('Mr.', 'Jones', 'pleasure', 5)
print("\n>> Format string\n",txt)


s='Hello {} {}, it is a great {} to meet you at {} o\' clock'
txt = s.format('Sir', 'Arthur', 'honor', 9)
print("\n>> Format string\n",txt)


s='I have a {food_item} and a {drink_item} with me'
txt = s.format(drink_item='soda', food_item='sandwich')
print("\n>> Format string\n",txt)
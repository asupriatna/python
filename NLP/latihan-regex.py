import re


s1 = 'Python is an excellent language'
s2 = 'I love the Python language. I also use Python to build applications at work!'

pattern = 'python'
# match only returns a match if regex match is found at the beginning of the string
res = re.match(pattern, s1)
print('\n',res)

# pattern is in lower case hence ignore case flag helps
# in matching same pattern with different cases
res = re.match(pattern, s1, flags=re.IGNORECASE)
print('\n',res)

# printing matched string and its indices in the original string
m = re.match(pattern, s1, flags=re.IGNORECASE)
print('\n','Found match {} ranging from index {} - {} in the string "{}"'.
    format(m.group(0), m.start(),m.end(), s1))

# match does not work when pattern is not there in the beginning of string s2
re.match(pattern, s2, re.IGNORECASE)

# illustrating find and search methods using the re module
res = re.search(pattern, s2, re.IGNORECASE)
print('\n',res)

print("\nString:", s2)
match_objs = re.finditer(pattern, s2, re.IGNORECASE)
for m in match_objs:
    print('Found match "{}" ranging from index {} - {}'.
    format(m.group(0),m.start(), m.end()))
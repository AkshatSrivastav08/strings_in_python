message="HELLO WORLD!"
print(message)
# there is difference b/w single and double quotes.
print(len(message))
# len is used to find length of the string.
print(message[6])
# indexing isb used to get the valueb in the string at particulaer value.
print(message[0:5])
# this is known as "slicing " where we work on a particular range.
print(message.upper())
print(message.lower())
# used to print in uppper and lower case.
print(message.count('L'))
#  count is used for the no. of times character occur in the string.
print(message.find("Hola"))
# it will give as index value -1 because it is not present in the string.
message= message.replace("WORLD", "Universe")
# replace is used to change your string at particular character.
print(message)
name= "Akshat"
greeting="Hello"
message= greeting + " " + name
print(message)
# + is used to adding two strings.
message="{}, {}. Welcome!".format(greeting, name)
print(message)
# this is used to foramt the stirng.
message='Bobby\'s world'
print(message)
# if we are using \ then it will skip the next part.

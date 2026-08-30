print("It's Time for Dinner")

# Multiline Strings """ """

a = """arbgbdybbty ftnhdtrnhdtn rnnurt n trnu r tnu rnu ru dfrsvrgverve ygetytsty yetyeywe"""
b = "I am Gonna Definitely going to Work in ISRO for Sure"
print(a)
print(a[3])
print(len(a))                       # len() is the func to give the length of the variable

for x in "Saran":
    print(x*10)


if "rnu" in a:
    print("It is There")
else:
    print('No')

print("rnu" in a)
print("zzz" not in a)

# Slicing strings

print(a[23:58])
print(a[:28])
print(a[5:])
print(a[-8:-61])

# Modify Strings

print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("i","S"))
print(b.split(" "))


print (a + b)

# Format Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt1 = f"The price is {price:.2f} dollars"
print(txt1)

# Escape Characters

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""

# String Methods

"""
capitalize()	         Converts the first character to upper case
casefold()	             Converts string into lower case
center()	             Returns a centered string
count()	                 Returns the number of times a specified value occurs in a string
encode()	             Returns an encoded version of the string
endswith()	             Returns true if the string ends with the specified value
expandtabs()	         Sets the tab size of the string
find()	                 Searches the string for a specified value and returns the position of where it was found
format()	             Formats specified values in a string
format_map()	         Formats specified values in a string
index()	                 Searches the string for a specified value and returns the position of where it was found
isalnum()	             Returns True if all characters in the string are alphanumeric
isalpha()	             Returns True if all characters in the string are in the alphabet
isascii()	             Returns True if all characters in the string are ascii characters
isdecimal()	             Returns True if all characters in the string are decimals
isdigit()	             Returns True if all characters in the string are digits
isidentifier()	         Returns True if the string is an identifier
islower()	             Returns True if all characters in the string are lower case
isnumeric()	             Returns True if all characters in the string are numeric
isprintable()	         Returns True if all characters in the string are printable
isspace()	             Returns True if all characters in the string are whitespaces
istitle()	             Returns True if the string follows the rules of a title
isupper()	             Returns True if all characters in the string are upper case
join()	                 Joins the elements of an iterable to the end of the string
ljust()	                 Returns a left justified version of the string
lower()	                 Converts a string into lower case
lstrip()	             Returns a left trim version of the string
maketrans()	             Returns a translation table to be used in translations
partition()	             Returns a tuple where the string is parted into three parts
replace()	             Returns a string where a specified value is replaced with a specified value
rfind()	                 Searches the string for a specified value and returns the last position of where it was found
rindex()	             Searches the string for a specified value and returns the last position of where it was found
rjust()	                 Returns a right justified version of the string
rpartition()	         Returns a tuple where the string is parted into three parts
rsplit()	             Splits the string at the specified separator, and returns a list
rstrip()	             Returns a right trim version of the string
split()	                 Splits the string at the specified separator, and returns a list
splitlines()	         Splits the string at line breaks and returns a list
startswith()	         Returns true if the string starts with the specified value
strip()	                 Returns a trimmed version of the string
swapcase()	             Swaps cases, lower case becomes upper case and vice versa
title()	                 Converts the first character of each word to upper case
translate()	             Returns a translated string
upper()	                 Converts a string into upper case
zfill()	                 Fills the string with a specified number of 0 values at the beginning

"""

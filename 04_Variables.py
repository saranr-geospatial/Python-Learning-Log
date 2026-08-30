x = 12             # type int
y = "Saran"        # type str
print(y,x)

x1 = str('3')
x2 = int(3)
x3 = float(3)
print(x1,x2,x3)
print(type(x3))

X = "A2d"         # Case Sensitive
print(X)

# Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
myvariabelename = "Saran"

# Assign Multiple Variables

a, b, c = "Saran", "NVIDIA", "A2D"
print(a,b,c)

d=e=f = "Insta"
print(d,e,f)

fruits = ["apple","banana"]
l, m = fruits
print(l)
print(m)

# Output Variables

o = "Python"
p = " is"
q = " a programming lang "
print(o+p+q)


# Global Variables

x = "Language"

def myfunc():
    global p
    p = "Hi"
    print(p)
    print("Python is a " + x)

myfunc()

print("Hello",p)
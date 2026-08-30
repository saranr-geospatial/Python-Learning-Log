# All Data Types

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

a = "Hello"
b = 20
c = 25
d = 66j
e = ["Saran","A2D"]
f = {"Saran","A2D"}
g = ("Saran","A2D")
i = range(12)
j = {"Name" : "Saran", "Age" : 18}
k = True
l = frozenset({"apple", "banana", "cherry"})		
m = b"Hello"		
n = bytearray(5)		
o = memoryview(bytes(5))	
p = None

print((a,b,c,d,e,f,g,i,j,k,l,m,n,o,p))
print(type(a,b,c,d,e,f,g,i,j,k,l,m,n,o,p))

# type() is used to typecasting
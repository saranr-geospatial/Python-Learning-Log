# Arithmetic Operators

'''
+	Addition		
-	Subtraction	
*	Multiplication	
/	Division	
%	Modulus		
**	Exponentiation		
//	Floor division
'''

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment Operators


'''
=	        x = 5	        x = 5	
+=	        x += 3	        x = x + 3	
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3	
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=     	x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 3)	x = 3
	
'''

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:                       # Warlus Operator
    print(f"List has {count} elements")


# Ternery Operator

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)
 
num = 6                                                # Can Be Used Insted of Elif
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)

# Comparision Operator

"""
==	Equal	                    x == y	
!=	Not equal	                x != y	
>	Greater than	            x > y	
<	Less than	                x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y	

"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

# Logiacal Operators

"""
and 	Returns True if both statements are true	                        x < 5 and  x < 10	
or	    Returns True if one of the statements is true	                    x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	            not(x < 5 and x < 10)
"""

x = 5
print(x > 0 and x < 10)
print(x > 0 or x < 10)
print(not x < 10)

# Idenify Operators

"""
is 	            Returns True if both variables are the same object	            x is y	
is not	        Returns True if both variables are not the same object	        x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)


# Membership Operators

"""
in 	        Returns True if a sequence with the specified value is present in the object	        x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	    x not in y
"""

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operator

"""
& 	AND	                    Sets each bit to 1 if both bits are 1		
|	OR	                    Sets each bit to 1 if one of two bits is 1	
^	XOR	                    Sets each bit to 1 if only one of two bits is 1	
~	NOT	                    Inverts all the bits	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	
>>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	
"""

print(6 & 3)
print(6 | 3)
print(6 ^ 3)

# Operator Precedence

print(100 + 5 * 3)         # Multiplication Has Precedence

## Precedence Order

"""
()	                                            Parentheses	
**	                                            Exponentiation	
+x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                                    Multiplication, division, floor division, and modulus	
+  -	                                        Addition and subtraction	
<<  >>	                                        Bitwise left and right shifts	
&	                                            Bitwise AND	
^	                                            Bitwise XOR	
|	                                            Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                                            Logical NOT	
and	                                            AND	
or	                                            OR	

"""

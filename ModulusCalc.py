print ('Hello, I am a modulus calculator')
print ('Would you like to see a tutorial? (press y for yes & n for no)')
yes = str(input())
decision='y'
if yes==decision:
    print ('') 
    print ('I can be used to find the remainder when (x^a + m^b) is divided by (y^c)')
    print ('For example ')
    print ('If x = 3, a = 2, m = 2, b = 1, y = 2, c = 2')
    print ('The computer will give the following results')
    print ('11 ≡ 3 (mod 4)')
    print ('Which is the same as - ')
    print ('(3^2 + 2^1) leaves a remainder of 3 when divided by (2^2)')
    print ('')

print ('Give me integer x ')
num1 = int(input())
print ('Give me the exponent of x')
num2 = int(input())
num3=num1**num2
print('What number m do you want to add to x?(add negative numbers for subtraction')
num4=int(input())
print('Give me the exponent of m')
num5=int(input())
num6=num3+num4**num5


print ('Give me integer y')
num7 = int(input())
print ('Give me the exponent of y')
num8 = int(input())
num9=num7**num8
num10=num6%num9
print( num6, '≡', num10, '(mod', num9, ' )')

eq1 = '4x^2 +4x +    (-8) =  0'
eq2 = '  x^2 +4x -    12 =  0'
eq3 = '  x^2 -10x +  9  =  0'
eq4 = ' x ^2 + x + 7 = 0'
eq5 = ' x^ 2 + 2 x +   1 = 0'

def quadratic_solver(eq):
    '''Solves quadratic equations of the form ax^2 + bx + c = 0'''
    eq = eq.lower() # all letters lowercase
    eq = eq.replace(' ','') # remove spaces
        
    a = eq[0:eq.index('x^2')].replace('(','').replace(')','')
    a = int(a) if a != '' else 1 # if a is not specified, it's equal 1
    b = eq[(eq.index('x^2+' if 'x^2+' in eq else 'x^2-')+4):eq.index('x+' if 'x+' in eq else 'x-')].replace('(','').replace(')','')
    b = int(b) if b != '' else 1 # if b is not specified, it's equal 1
    c = eq[(eq.index('x+' if 'x+' in eq else 'x-')+2):eq.index('=')].replace('(','').replace(')','')
    c = int(c if 'x+' in eq else '-'+c)
    
    print('Your equation:', eq)
    d = (b**2) - (4*a*c) # discriminant
    if d < 0:
        return 'No real roots\n'
    elif d == 0:
        return f'One real root:\n {-b/(2*a)}\n'
    else:
        return f'Two real roots:\n {(-b + d**0.5)/(2*a)} \n {(-b - d**0.5)/(2*a)}\n'

print(quadratic_solver(eq1))
print(quadratic_solver(eq2))
print(quadratic_solver(eq3))
print(quadratic_solver(eq4))
print(quadratic_solver(eq5))
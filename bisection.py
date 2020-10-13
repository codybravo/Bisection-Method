from math import *
import sigfig

def lock():
    global count
    decison = input("do you want to lock interval:")
    print("")
    if decison == "n":
        expression(exp)
    elif decison == "y":
        count += 1
        if expression.evl_exp < 0:
            lock.a = expression.x
        elif expression.evl_exp > 0:
            lock.b = expression.x
        
        if count != 2 :
            expression(exp)
    return lock.a,lock.b
    
def expression(express):
    x = float(input("x="))
    expression.x = x
    expression.evl_exp = eval(exp)
    print(exp,"=",expression.evl_exp)
    lock()

def significant(q,r):
    bisect.exp1 = sigfig.round(q,r)
    return bisect.exp1
    
def decimal(q,r):
    bisect.exp1 = round(q,r)
    return bisect.exp1
    
    
def bisect(expresso):
    global count2
    global d 
    global exp2
    global correction
    x = (lock.a + lock.b)/2
    f = eval(exp)
    if correction == 1:
        decimal(x,d)
    elif correction == 2:
        significant(x,d)
    
    print('{: <5}'.format(count2),'{: <15}'.format(round(lock.a,11)),'{: <15}'.format(round(lock.b,11)),'{: <15}'.format(round(x,11)),'{: <15}'.format(round(f,11)))
    count2 += 1
    if f < 0:
        lock.a = x
    elif f > 0:
        lock.b = x 
    
    if bisect.exp1 != exp2:
        exp2 = bisect.exp1
        bisect(exp)
    return bisect.exp1

exp2 = 0
count = 0  
count2 = 0
exp = input("enter expression:")
print("""what type of correction required
         1. Decimal places
         2. Significant figures""")
correction = int(input("enter number:"))
d = int(input("correction:"))
print("")
expression(exp)
print('{: <5}'.format("i"),'{: <15}'.format("a(-ve)"),'{: <15}'.format("b(+ve)"),'{: <15}'.format("x"),'{: <15}'.format("f(x)"))
print("_"*75)
bisect(exp)
print("")
print("root of the given equation is",bisect.exp1)


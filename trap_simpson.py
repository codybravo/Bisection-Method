import sigfig
class numerical(object):
    def __init__(self):
        self.x_list = []
        self.f_list = []
    
    def value_x(self,x,h,exp):
        for i in range(0,n+1):
            self.x_list.append(round(x,10))
            self.f_list.append(round(eval(exp),10))
            x += h
        
        return self.x_list,self.f_list
        
class T_and_S(object):
    def __init__(self):
        self.sum1,self.sum2,self.sum3 = 0,0,0
        self.y1 = ["-" for i in range(n+1)]
        self.y2 = list(self.y1)
        self.y3 = list(self.y1)
        self.i = 0
        self.blank = " "
     
    def significant(self,correction,d):
        if correction == 1:
            self.i = round(self.i,d)
        elif correction == 2:
            self.i = sigfig.round(self.i,d)
        return self.i
            
    def simson_y(self,x_list,f_list):
        
        print("Simpson's (1/3)rd Rule",end="\n\n")
        print('{:-<75}'.format("-"))
        print('{: <4}'.format("i"),'{: <13}'.format("x"),'{: <13}'.format("f(x)"),'{: <13}'.format(f'y(i=0,{n})'),'{: <13}'.format("y(i=1,3,5,..)"),'{: <13}'.format("y(i=2,4,6,..)"))
        print('{:-<75}'.format("-"))

        for i in range(0,n+1):
            if (i == 0 or i == n): 
                self.y1[i] = round(f_list[i],10)
                self.sum1 += self.y1[i]
        
        for i in range(1,n,2):
            self.y2[i] = round(f_list[i],10)
            self.sum2 += self.y2[i]
            
        for i in range(2,n,2):
            self.y3[i] = round(f_list[i],10)
            self.sum3 += self.y3[i]
    
        for i in range(0,n+1):
            print('{: <4}'.format(i),'{: <13}'.format(x_list[i]),'{: <13}'.format(f_list[i]),'{: <13}'.format(self.y1[i]),'{: <13}'.format(self.y2[i]),'{: <13}'.format(self.y3[i]))
        
        print('{:-<75}'.format("-"))
    
        self.i = (h/3)*(self.sum1+(4*self.sum2)+(2*self.sum3))
        
        self.significant(correction,d)
        
        print(f''' 
Now by Simpson's (1/3)rd Rule,
I = h/3[(y0+yn+(4×(y1+y3+y5+..))+(2*(y2+y4+..))]  
I = {h}/3[{self.sum1}+(4*{self.sum2})+(2*{self.sum3})]
I = {self.i}

''')

        return self.blank
    
    
    def trapezoidal_y(self,x_list,f_list):
        
        print("Trapezoidal's Rule",end="\n\n")
        print('{:-<75}'.format("-"))
        print('{: <4}'.format("i"),'{: <13}'.format("x"),'{: <13}'.format("f(x)"),'{: <13}'.format("y(i=0,1)"),'{: <13}'.format("y(i=1,..,n-1)"))
        print('{:-<75}'.format("-"))
        
        for i in range(0,n+1):
            if (i == 0 or i == n): 
                self.y1[i] = round(f_list[i],10)
                self.sum1 += self.y1[i] 
                
        for i in range(1,n):
            self.y2[i] = round(f_list[i],10)
            self.sum2 += self.y2[i]
            
        for i in range(0,n+1):
            print('{: <4}'.format(i),'{: <13}'.format(x_list[i]),'{: <13}'.format(f_list[i]),'{: <13}'.format(self.y1[i]),'{: <13}'.format(self.y2[i]))
        
        print('{:-<75}'.format("-"))
        
        self.i = (h/2)*((self.sum1)+(2*self.sum2))
        
        self.significant(correction,d)
        
        print(f''' 
Now by Trapezoidal Rule,
I = h/2[(y0+y{n}+2(y1+y2+y3+...+y{n-1})]
I = {h}/2[({self.sum1}+2*{self.sum2})
I = {self.i}

''')
        
        return self.blank

print("""what type of correction required
         1. Decimal places
         2. Significant figures""")
correction = int(input("enter number:"))
d = int(input("correction:"))
print("")
print("enter limits of integration")
a = float(input("a:"))
b = float(input("b:"))
n = int(input("enter no. of subinterval, n:"))
print("h = (b-a)/n")
h = (b-a)/n
print(f'h={h}')
x = 0 + a
exp = input("enter expression:")
print("")
t = numerical()
x_list,f_list = t.value_x(x,h,exp) 
print(T_and_S().simson_y(x_list,f_list)) 
print(T_and_S().trapezoidal_y(x_list,f_list))



    


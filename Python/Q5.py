# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 22:46:43 2022

@author: Amirhossein
"""
import itertools
import math

class Shape:
    newid = itertools.count()

    def __init__(self):
        self.id = next(self.newid)

    @classmethod   
    def perimeter(self):
        return None
    
      
    def area(self):
        return None 
    
    def print(self):
        print("\n\nName:", type(self).__name__)
        print("Id:", self.id)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area(), "")
        

class Circle(Shape):
    
    def __init__(self,r: float):
        if ( r < 0):
            print("Error: Invalid Circle")
            Shape.__init__(self)
            return None
        else: 
            self.radius = r
            super().__init__()
        
        
    def perimeter(self):
        try:
            return math.pi * self.radius * 2 
        except:
            return None
            
        
  
    def area(self):
        try:
            return math.pi * self.radius**2
        except:
            return None
    
    
    
class Ellipse(Shape):
    
    def __init__(self,a: float, b: float):
        if (float(min(a, b)) < 0):
            print("Error: Invalid Ellispe")
            Shape.__init__(self)
            return None
        else: 
            self.semiMajor = max(a, b)
            self.semiMinor = min(a, b)
            super().__init__()
        
        
    def perimeter(self):
        pass
  
    def area(self):
        try:
            return math.pi * self.semiMajor * self.semiMinor
        except:
            return None
     
    def eccentricity(self):
        try:
            return math.sqrt( self.semiMajor**2 - self.semiMinor**2)
        except: 
            return None
   
    def print(self):
        super().print()
        print("Eccentricity:", self.eccentricity())
        
class Rhombus(Shape):
    
    def __init__(self,d1: float,d2: float):
        if (float(min(d1, d2)) < 0):
            print("Error: Invalid Rhombus")
            Shape.__init__(self)
            return None
        else:
            self.diagonal1 = d1
            self.diagonal2 = d2
            super().__init__()
        
        
    def perimeter(self):
        try:
            return 2 * (math.sqrt(self.diagonal1**2 + self.diagonal2**2))
        except:
            return None
  
    def area(self):
        try:
            return ( self.diagonal1 * self.diagonal2)/2
        except:
            return None
     
    def inradius(self):
        try:
            return self.diagonal1 * self.diagonal2 / (2 * (self.diagonal1**2 + self.diagonal2**2)**(1/2))
        except: 
            return None 
        
    def print(self):
        super().print()
        print("Inradius:", self.inradius())


"""
    
a = Shape()
a.print()  
a1 = Shape()
a1.print() 
print( a.perimeter()   ) 
a2 = Circle(10)
a2.print() 
print( a2.perimeter()   ) 
print("\n****\n")
a3 = Ellipse(10,100)

a3.print() 

a4 = Rhombus(10,5)

a4.print() 
"""

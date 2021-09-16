class Shape:

    def __init__(self, p_base, p_height):

        self.base = p_base
        self.height = p_height

        def area(self):
            print("my superpower revealed to me that I wont be used ... sobs")

class Area_paralellogram(Shape):
    def __init__(self, p_base, p_height):
        super().__init__(p_base, p_height) 
    
    def areapara(self):
        print("The area of paralellogram is {}".format(self.base * self.height ))

class peri_Trapezoid(Shape):
    def __init__(self, p_base, p_height, base1, height1 ):
        super().__init__(p_base, p_height)
        self.base1 = base1
        self.height1 = height1 
    
    def peri_par(self):
        return("The perimeter of the trapezium is {}".format(self.base + self.height + self.base1 + self.height1))

class Triangle(Shape):
    def __init__(self, p_base, p_height):
        super().__init__(p_base, p_height) 

    def area(self):
        return("The area of the triangle is {}".format((self.base * self.height)/2))

    

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        if(isinstance(other, type(self))):
            return Vector(int(self.x + other.x), int(self.y + other.y), int(self.z + other.z))
        

    def __mul__(self, other):
        if(isinstance(other, int)):
            return Vector(other * self.x, other * self.y, other*self.z)
        elif(isinstance(other, Vector)):
            return self.x*other.x + self.y*other.y + self.z*other.z

    def __xor__(self, other):
        # cross product a^b
        return Vector(self.y*other.z - self.z*other.y,
                      self.z*other.x - self.x*other.z,
                      self.x*other.y - self.y*other.x)

    def __str__(self):
        return f"{(self.x, self.y, self.z)}"
    
    def __repr__(self):
        return f"{(self.x, self.y, self.z)}"

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2  + self.z ** 2) ** 0.5

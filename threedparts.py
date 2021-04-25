from vector import *

class Triangle():
    def __init__(self, p1, p2, p3):
        self.points = (p1, p2, p3)
    
    def __str__(self):
        return f"{(self.points)}"
    
    def __call__(self, arg=None):
        if(isinstance(arg, int)):
            return self.points[arg]
        else:
            return self.points

class Mesh():
    def __init__(self, tris):
        self.triangles = tris
        
    def __str__(self):           
        for t in self.triangles:
            print(t)
        return ""

def cube():
    verticies =[Triangle(Vector(1,-1,-1), Vector(-1,1,-1), Vector(-1,-1,-1)),
                Triangle(Vector(1,-1,-1), Vector(1,1,-1), Vector(-1,1,-1)),
                Triangle(Vector(1,1,-1), Vector(-1,1,1), Vector(-1,1,-1)),
                Triangle(Vector(1,1,-1), Vector(1,1,1), Vector(-1,1,1)),
                Triangle(Vector(1,-1,1), Vector(1,1,-1), Vector(1,-1,-1)),
                Triangle(Vector(1,-1,1), Vector(1,1,1), Vector(1,1,-1)),
                Triangle(Vector(1,-1,1), Vector(-1,1,1), Vector(-1,-1,1)),
                Triangle(Vector(1,-1,1), Vector(1,1,1), Vector(-1,1,1)),
                Triangle(Vector(-1,-1,1), Vector(-1,1,-1), Vector(-1,-1,-1)),
                Triangle(Vector(-1,-1,1), Vector(-1,1,1), Vector(-1,1,-1))]

    return Mesh(verticies)
    
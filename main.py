import tkinter as tk

class Vector():
    def __init__(self, x, y, z):
        self.pos = (x, y, z)
    
    def __add__(self, other):
        if(type(self) == type(other)):
            return Vector(self.pos[0] + other.pos[0], self.pos[1] + other.pos[1], self.pos[2] + other.pos[2])
    
    def __repr__(self):
        return f"{(self.pos)}"

class Triangle():
    def __init__(self, p1, p2, p3):
        self.points = (p1, p2, p3)
    
    def __repr__(self):
        return f"{(self.points)}"

class Mesh():
    def __init__(self, tris):
        self.triangles = tris
    
    def __repr__(self):           
        for t in self.triangles:
            print(t)
        return ""
    
    def __str__(self):           
        for t in self.triangles:
            print(t)
        return ""



class Engine():
    def __init__(self):
        self.window = tk.Tk()
        self.window.mainloop()


tris = [Triangle(Vector(0, 0, 0), Vector(1, 0, 0), Vector(0, 1, 0)), Triangle(Vector(1, 1, 0), Vector(1, 0, 0), Vector(0, 1, 0))]

square = Mesh(tris)

print(square)

e = Engine()
import tkinter as tk
from vector import *
from matrix import *
from threedparts import *

class Engine():
    def __init__(self, mesh):
        self.root = tk.Tk()
        self.height, self.width = 750, 750
        self.scale = 100
        self.canvas = tk.Canvas(self.root, bg="black", height=self.height, width=self.width)
        self.render(mesh)
        self.canvas.pack()
        self.root.mainloop()

    def rotate(self, v, theta):
        rm = Matrix([0]).rotMat(theta)
        return rm* v


    
    def draw_line(self, v1, v2):
        shiftx = int(self.width/2)
        shifty = int(self.height/2)
        v1 = self.rotate(v1, 45)
        v2 = self.rotate(v2, 45)

        self.canvas.create_line(((v1.x*self.scale) + shiftx)/v1.z, ((v1.y*self.scale) + shifty)/v1.z, ((v2.x*self.scale) + shiftx)/v2.z, ((v2.y*self.scale) + shifty)/v2.z, fill="green")

    def render(self, mesh):
        self.obj = mesh
        for i in range(len(mesh.triangles)):
            triangle = mesh.triangles[i]
            self.draw_line(triangle(0), triangle(1))
            self.draw_line(triangle(1), triangle(2))
            self.draw_line(triangle(2), triangle(0))
        
                


def test():
    Engine(cube())

test()
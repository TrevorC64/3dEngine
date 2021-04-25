class Triangle():
    def __init__(self, p1, p2, p3):
        self.points = (p1, p2, p3)
    
    def __str__(self):
        return f"{(self.points)}"

class Mesh():
    def __init__(self, tris):
        self.triangles = tris
        
    def __str__(self):           
        for t in self.triangles:
            print(t)
        return ""
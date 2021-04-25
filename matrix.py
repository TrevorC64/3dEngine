from vector import *
from math import *

def generate_2darray(rows, cols):
    new = []
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(0)
        new.append(r)
    return new


class Matrix():
    def __init__(self, matx):
        self.matrix = matx

    def get_size(self):
        return f"{len(self.matrix)} x {len(self.matrix[0])} (row x col)"

    def __str__(self):           
        for row in range(0, len(self.matrix)):
            r = []
            for col in range(0, len(self.matrix[0])):
                r.append(self.matrix[row][col])
            print(r)
        return ""
    
    def __mul__(self, other):
        if(isinstance(other, int)):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j] *= other 
        elif(isinstance(other, Vector)):  
            x = self.matrix[0][0] * other.x + self.matrix[0][1] * other.y + self.matrix[0][2] * other.z
            y = self.matrix[1][0] * other.x + self.matrix[1][1] * other.y + self.matrix[1][2] * other.z
            z = self.matrix[2][0] * other.x + self.matrix[2][1] * other.y + self.matrix[2][2] * other.z
            return Vector(x,y,z)

        elif(isinstance(other, Matrix)):  
            rows, cols = (len(self), len(other[0]))
            res = generate_2darray(rows, cols)

            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        res[i][j] += self.matrix[i][k] * other.matrix[k][j]
        
            return Matrix(res)
    
    def mvMatrix(self):
        return Matrix([[int(3.14/2), 1, 0, 100],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 1]])
    
    def rotMat(self, theta):
        return Matrix([[cos(radians(theta)), -1*sin(radians(theta)), 0],[sin(radians(theta)), cos(radians(theta)), 0],[0,0,1]])
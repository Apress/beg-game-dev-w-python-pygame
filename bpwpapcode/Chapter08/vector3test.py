from gameobjects.vector3 import *

A = Vector3(6, 8, 12)
B = Vector3(10, 16, 12)

print "A is", A
print "B is", B
print "Length of A is", A.get_magnitude()
print "A+B is", A+B
print "A-B is", A-B
print "A normalized is", A.get_normalized()
print "A*2 is", A * 2

class Vector3(object):
    
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, rhs):
        
        return Vector3(self.x + rhs.x, self.y + rhs.y, self.y + rhs.y)
    
    def __sub__(self, rhs):
        
        return Vector3(self.x - rhs.x, self.y - rhs.y, self.y - rhs.y)
    
def isographic_projection(vector3):
    
    return (vector3.x, vector3.y)

def perspective_projection(vector3, d):
    
    x, y, z = vector3    
    return (x * d/z, y * d/z)
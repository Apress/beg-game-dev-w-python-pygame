import math

A = (10.0, 20.0)
B = (30.0, 35.0)
AB = (B[0]-A[0], B[1]-A[1])

print "AB is", AB

def vector_magnitude(vec):    
    return math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
    
print "Magnitude of AB is", vector_magnitude(AB)

def unit_vector(vec):
    magnitude = vector_magnitude(vec)
    return (vec[0] / magnitude, vec[1] / magnitude)
    
print "Unit vector of AB is (%s, %s)" % unit_vector(AB)

from gameobjects.vector3 import *

A = (-6, 2, 2)
B = (7, 5, 10)
plasma_speed = 100. # meters per second

AB = Vector3.from_points(A, B)
print "Vector to droid is", AB

distance_to_target = AB.get_magnitude()
print "Distance to droid is", distance_to_target, "meters"

plasma_heading = AB.get_normalized()
print "Heading is", plasma_heading

time_to_target = distance_to_target / plasma_speed
print "Time to hit droid is", time_to_target, "seconds"

#bolt_location += plasma_heading * time_passed_seconds + plasma_speed
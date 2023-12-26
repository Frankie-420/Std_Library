def area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    
    return area

def area_of_rectangle(length,width):
    # Calculate the semi-perimeter
    area = length*width
    return area

def cube_m2(area,height):
    cubic_area = area*height
    return cubic_area

def cubic_weight(area,weight):
    cubic_weight = area*weight
    return cubic_weight

WEIGHT = 750 # KG/m
THICKNESS = 0.0016 # m

Rectangles = ((0.5,0.5),(0.5,0.5)) # m
Triangles = ((0.5,0.5,0.5),(0.5,0.5,0.5)) # m

total = 0
for a,b,c in Triangles:
    area = area_of_triangle(a,b,c)
    cubic_area = cube_m2(area,THICKNESS)
    cubed_weight = cubic_weight(cubic_area,WEIGHT)
    total = total + cubed_weight

for length,Width in Rectangles:
    area = area_of_rectangle(length,Width)
    cubic_area = cube_m2(area,THICKNESS)
    cubed_weight = cubic_weight(cubic_area,WEIGHT)
    total = total + cubed_weight

print(total)

def area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    
    return area

def area_of_rectangle(length: float,width: float) -> float:
    # Calculate the semi-perimeter
    return length * width

def cube_m2(area:float,height:float) -> float:
    cubic_area = area*height
    return cubic_area

def get_cubic_weight(area,weight):
    cubic_weight = area*weight
    return cubic_weight

def calculate_volume_of_cuboid(length_a, length_b, length_c):
    """
    Calculate the volume of a three-dimensional rectangle (cuboid).

    Parameters:
    - length_a (float): Length along the first dimension.
    - length_b (float): Length along the second dimension.
    - length_c (float): Length along the third dimension.

    Returns:
    float: Volume of the cuboid.
    """
    volume = length_a * length_b * length_c
    return volume

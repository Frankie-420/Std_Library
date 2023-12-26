def calculate_area_of_triangle(side_a, side_b, side_c):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    - side_a (float): Length of the first side.
    - side_b (float): Length of the second side.
    - side_c (float): Length of the third side.

    Returns:
    float: Area of the triangle.
    """
    # Calculate the semi-perimeter
    semi_perimeter = (side_a + side_b + side_c) / 2
    
    # Calculate the area using Heron's formula
    area = (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))**0.5
    
    return area

def calculate_area_of_rectangle(length: float, height: float) -> float:
    """
    Calculate the area of a rectangular prism.

    Parameters:
    - length (float): Length of the rectangle.
    - height (float): Height of the prism.

    Returns:
    float: Area of the rectangular prism.
    """
    rectangle_area = length * height
    return rectangle_area

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

def calculate_cubic_weight(length: float, weight: float) -> float:
    """
    Calculate the cubic weight of an object.

    Parameters:
    - length (float): Length of the object.
    - weight (float): Weight of the object.

    Returns:
    float: Cubic weight of the object.
    """
    cubic_weight = length * weight
    return cubic_weight

from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot ne negative.")
    return pi * (r ** 2)

# Test function
# radii = [2, 0, -6, 1 + 3j, False, True, "radius"]
# message = "Area of circles with r = {radius} is {area}."

# for r in radii:
#     A = circle_area(r)
#     print(message.format(radius=r, area=A))
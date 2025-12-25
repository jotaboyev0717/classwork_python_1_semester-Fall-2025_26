def rectangle_area(width, height):
    area = width * height
    return area

def rectangle_perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter

def volume_prism(base, triangle_height, prism_length):
    triangle_area = 0.5 * base * triangle_height
    volume = triangle_area * prism_length
    return volume
w = 5
h = 8
area = rectangle_area(w, h)
perimeter = rectangle_perimeter(w, h)
print(f"Rectangle {w}*{h}:")
print(f"    Area: {area}")
print(f"    Perimeter: {perimeter}")

b = 6
th = 4
pl = 10
volume = volume_prism(b, th, pl)
print(f"Tringular prism (base={b}, height={th}, length={pl}):")
print(f"    Volume: {volume}")
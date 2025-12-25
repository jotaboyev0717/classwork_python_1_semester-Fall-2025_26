def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit

def fahrenheit_celcius_to(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius
c1 = 0
f1 = celcius_to_fahrenheit(c1)
print(f"{c1}°C = {f1}°F")
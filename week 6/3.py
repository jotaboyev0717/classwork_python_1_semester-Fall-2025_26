# # --- Example 8: Nested Loops ---
# print("\n--- Drawing a 4x5 Rectangle ---")
# height = 4
# width = 5

# # The outer loop controls the rows
# for row_num in range(height):
#     # The inner loop controls the columns for the CURRENT row
#     for col_num in range(width):
#         # The 'end' parameter prevents print() from adding a newline
#         print("* ", end="")
        
#     # After the inner loop finishes, print a newline to move to the next row
#     print()

# print("--- Triangle Pattern Printer ---")
# height = int(input("Enter the desired height of the triangle: "))

# for i in range(1, height + 1):
#     for j in range(i):
#         print("* ", end="")
#     print()  # yangi qatorga o‘tish uchun

# print("--- Triangle Pattern Printer ---")

# height = 5 

# for i in range(1, height + 2:
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(start, end, step):
#     print(i)
readings = [
    ('SensorB', 25.4),
    ('SensorA', 22.1),
    ('SensorB', 26.1),
    ('SensorC', 30.5),
    ('SensorA', 21.9),
    ('SensorB', 25.9)
]
for sensor, temp in readings:
    print(sensor)

def remove_outliers(data, min_val, max_val):
    i = 0
    while i < len(data):
        if data[i] < min_val or data[i] > max_val:
            data.pop(i)   
        else:
            i += 1      

measurements = [8, 5, 12, 1, 9, 20, 15]
print("Original measurements:", measurements)
remove_outliers(measurements, 5, 15)
print("Cleaned measurements: ", measurements)
print("--------------------")


temps = [-5, 10, 0, 35, 15, 40, 20]
print("Original temps:", temps)
remove_outliers(temps, 0, 30)
print("Cleaned temps: ", temps)
print("--------------------")


edge_case = [100, 1, 101, 2, 102]
print("Original edge case:", edge_case)
remove_outliers(edge_case, 0, 10)
print("Cleaned edge case: ", edge_case)

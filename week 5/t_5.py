def calculate_moving_average(data, window_size):
    new_list = []
    
    if window_size <= 0 or window_size > len(data):
        return []
    
    for i in range(len(data)-window_size+1):
        triple = data[i:i+window_size]
        new_list.append(sum(triple)/window_size)
    return new_list

print(calculate_moving_average([1, 2, 3, 4, 5], 2))
print(calculate_moving_average([10, 20, 30, 40, 50], 3))
print(calculate_moving_average([5, 10, 15], 5))
print(calculate_moving_average([8, 12], 1))
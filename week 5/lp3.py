def reverse_list_in_place(data_list):
    left = 0
    right = len(data_list) - 1
    while right > left:
        data_list[left], data_list[right] = data_list[right], data_list[left]
        left += 1
        right -= 1
    return data_list



letters = ['a', 'b', 'c', 'd', 'e']
print(reverse_list_in_place(letters))
numbers = [1, 2, 3, 4]
print(reverse_list_in_place(numbers))
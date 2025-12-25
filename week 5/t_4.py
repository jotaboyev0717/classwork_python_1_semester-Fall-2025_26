def find_longest_run(data):
    if not data:
        return 0
    max_run = 1
    current_run = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 1
    return max_run
print(find_longest_run([1, 2, 2, 3, 3, 3, 2, 2]))      # 3
print(find_longest_run(['A', 'A', 'A', 'B', 'C']))    # 3
print(find_longest_run([5, 5, 5, 5, 5]))               # 5
print(find_longest_run([1, 2, 3, 4, 5]))               # 1
print(find_longest_run([]))                            # 0

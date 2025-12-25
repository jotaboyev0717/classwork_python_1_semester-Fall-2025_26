def zigzag_merge(list1, list2):
    new_list = []
    i = 0
    while i < len(list1) or i < len(list2):
        if i < len(list1):
            new_list.append(list1[i])
        if i < len(list2):
            new_list.append(list2[i])
        i +=1
        
    # for i in range(min(len(list1), len(list2))):
    #     new_list.append(list1[i])
    #     new_list.append(list2[i])
    # new_list.extend(list1[min(len(list1), len(list2)):])
    # new_list.extend(list2[min(len(list1), len(list2)):])
    return new_list
list_a = [1, 2, 3]
list_b = ['A', 'B', 'C']
print(zigzag_merge(list_a, list_b))

list_c = [1, 2]
list_d = ['A', 'B', 'C', 'D']
print(zigzag_merge(list_c, list_d))
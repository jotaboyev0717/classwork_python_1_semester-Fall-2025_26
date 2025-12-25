# def zigzag_merge(list1, list2):
#     merged = []  # new list to store result
#     length = max(len(list1), len(list2))  # find longer length

#     for i in range(length):
#         if i < len(list1):      # ad1d from list1 if exists
#             merged.append(list1[i])
#         if i < len(list2):      # add from list2 if exists
#             merged.append(list2[i])
    
#     return merged
    

def zigzag_merge(list1, list2):
    merged = []
    i = 0  # indeksni 0 dan boshlaymiz

    # sikl ikkala list tugamaguncha davom etadi
    while i < len(list1) or i < len(list2):
        if i < len(list1):      # agar list1 da hali element bo‘lsa
            merged.append(list1[i])
        if i < len(list2):      # agar list2 da ham hali element bo‘lsa
            merged.append(list2[i])
        i += 1  # keyingi elementga o‘tamiz

    return merged

list_a = [1, 2, 3]
list_b = ['A', 'B', 'C', 'D']
print(zigzag_merge(list_a, list_b))
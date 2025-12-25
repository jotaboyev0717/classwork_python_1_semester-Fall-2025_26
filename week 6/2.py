def get_top_n_frequent(items, n):
    unique = []
    counts = []

    for item in items:
        if item not in unique:
            unique.append(item)
            counts.append(1)
        else:
            index = unique.index(item)
            counts[index] += 1

    # eng ko‘p chiqadiganlarni topish
    result = []

    for _ in range(min(n, len(unique))):
        max_count = -1
        max_item = ""

        for i in range(len(unique)):
            if counts[i] > max_count:
                max_count = counts[i]
                max_item = unique[i]
            elif counts[i] == max_count and unique[i] < max_item:
                max_item = unique[i]

        result.append(max_item)

        idx = unique.index(max_item)
        unique.pop(idx)
        counts.pop(idx)

    return result

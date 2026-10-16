def rotate_list(items, k):
    if len(items) == 0:
        return []
    k = k % len(items)
    if k == 0:
        return list(items)
    return items[-k:] + items[:-k]
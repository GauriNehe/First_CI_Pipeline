def is_anagram(first, second):
    a = first.replace(" ", "").lower()
    b = second.replace(" ", "").lower()
    return sorted(a) == sorted(b)
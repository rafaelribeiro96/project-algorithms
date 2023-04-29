def merge(left, right):
    array = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            array.append(left[0])
            left = left[1:]
        else:
            array.append(right[0])
            right = right[1:]

    array += left
    array += right

    return array


def is_anagram(first_string, second_string):
    first_string_sortered = sort_list(list(first_string.lower()))
    second_string_ordered = sort_list(list(second_string.lower()))
    return (
        "".join(first_string_sortered),
        "".join(second_string_ordered),
        are_words_equal(
            "".join(first_string_sortered),
            "".join(second_string_ordered),
        ),
    )


def are_words_equal(w1, w2):
    return bool(w1 and w2 and w1 == w2)


def sort_list(lettt):
    if len(lettt) <= 1:
        return lettt

    mid = len(lettt) // 2
    left = lettt[:mid]
    right = lettt[mid:]
    left = sort_list(left)
    right = sort_list(right)

    return merge(left, right)

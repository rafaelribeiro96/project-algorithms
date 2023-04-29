def is_palindrome_recursive(w, li, hi):
    if len(w) == 0:
        return False
    elif w[li] != w[hi]:
        return False
    elif li >= hi:
        return True
    else:
        return is_palindrome_recursive(w, li + 1, hi - 1)


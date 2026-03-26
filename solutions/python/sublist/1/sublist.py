# Possible sublist categories.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    def is_sublist(a, b):
        if len(a) == 0:
            return True
        for i in range(len(b) - len(a) + 1):
            if b[i:i + len(a)] == a:
                return True
        return False

    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    elif is_sublist(list_one, list_two):
        return SUBLIST
    else:
        return UNEQUAL
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

values = [100, "PASS", [1, 2], {1, 2}, (1, 2), frozenset([1, 2])]
for v in values:
    print(v, "->", is_hashable(v))
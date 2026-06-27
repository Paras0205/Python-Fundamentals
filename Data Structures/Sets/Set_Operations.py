a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1.Add / remove elements

a.add(10)       # add one element
a.remove(2)     # remove 2 (error if missing)
a.discard(2)    # remove 2 (no error if missing)
a.clear()       # empty the set

# 2.Membership

if 3 in a:
    print("3 is present")

# 3.Union (combine)

a_union_b = a | b       # {1, 2, 3, 4, 5, 6}

# 4.Intersection (common)

a_inter_b = a & b       # {3, 4}

# 5.Difference (in a but not in b)

a_diff_b = a - b        # {1, 2}
b_diff_a = b - a        # {5, 6}

# 6.Symmetric difference (in one, but not both)

sym_diff = a ^ b        # {1, 2, 5, 6}
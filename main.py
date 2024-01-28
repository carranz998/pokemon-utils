from pokemon_statistics import get_ordered_types

for a in get_ordered_types():
    combination = a['combination']
    coefficients = sorted(set(a.keys()) - set(['combination']), reverse=True)

    print(combination)
    print(a)
    cs = {}
    for c in coefficients:
        try:
            number_of_weakness = len(a[c])
        except TypeError:
            number_of_weakness = 0

        cs[c] = number_of_weakness

    print(cs.items())

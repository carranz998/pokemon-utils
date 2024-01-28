from itertools import combinations

import pandas as pd

from data_warehouse.repositories import Type_Chart_Repository


def get_ordered_types():
    all_pokemon_tyes = Type_Chart_Repository.get_all_pokemon_types()

    all_defense_efectivess = {}

    for combination in combinations(all_pokemon_tyes, 2):
        defense_efectivess = Type_Chart_Repository \
            .get_defensive_efectiveness(combination)

        swapped_dict = {}
        for key, value in defense_efectivess.items():
            swapped_dict.setdefault(value, []).append(key)

        all_defense_efectivess[combination] = swapped_dict

    rows = []
    for combination, values in all_defense_efectivess.items():
        row_dict = {'combination': combination}
        row_dict.update(values)
        rows.append(row_dict)

    df = pd.DataFrame(rows)
    coefficient_columns = list(set(df.columns) - set(['combination']))
    coefficient_columns = sorted(coefficient_columns, reverse=True)

    sorted_df = df.sort_values(
        by=coefficient_columns,
        key=lambda x: x.str.len(),
        ascending=False
    )

    for _, row in sorted_df.iterrows():
        row_dict = row.to_dict()
        yield row_dict

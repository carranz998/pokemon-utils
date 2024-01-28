from itertools import combinations
from typing import Any, Dict, List

import pandas as pd

from data_warehouse.repositories import Type_Chart_Repository


def get_ordered_types():
    all_pokemon_tyes = Type_Chart_Repository.get_all_pokemon_types()

    all_defense_efectiveness = {}

    for combination in combinations(all_pokemon_tyes, 2):
        defense_efectivess = Type_Chart_Repository \
            .get_defense_efectiveness(list(combination))

        all_defense_efectiveness[combination] = __swap_dict(defense_efectivess)

    rows = __flat_coefficients(all_defense_efectiveness)

    df = pd.DataFrame(rows)
    sorted_df = __sort_by_coefficients(df)

    for _, row in sorted_df.iterrows():
        row_dict = row.to_dict()
        yield row_dict


def __flat_coefficients(all_defense_efectiveness: Dict[Any, List[Any]]) -> List[Dict[Any, Any]]:
    rows = []

    for combination, values in all_defense_efectiveness.items():
        row_dict = {'combination': combination}
        row_dict.update(values)
        rows.append(row_dict)

    return rows


def __sort_by_coefficients(df: pd.DataFrame) -> pd.DataFrame:
    coefficient_columns = list(set(df.columns) - set(['combination']))
    coefficient_columns = sorted(coefficient_columns, reverse=True)

    sorted_df = df.sort_values(
        by=coefficient_columns,
        key=lambda x: x.str.len(),
        ascending=False
    )

    return sorted_df


def __swap_dict(dictionary: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    swapped_dict: Dict[Any, Any] = {}

    for key, value in dictionary.items():
        swapped_dict.setdefault(value, []).append(key)

    return swapped_dict

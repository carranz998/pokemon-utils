import csv
from typing import Dict, List

from data_warehouse.engines import Matrix_Subset_Builder


class Type_Chart_Repository:
    @classmethod
    def get_all_pokemon_types(cls) -> List[str]:
        with open('type_chart.csv', 'r') as file:
            complete_csv_content = list(csv.reader(file))

        all_pokemon_types = (
            Matrix_Subset_Builder(complete_csv_content)
            .add_rows(0)
            .delete_columns(0)
            .build_subset()
            .flatten()
            .matrix_subset
        )

        return all_pokemon_types

    @classmethod
    def get_attack_efectiveness(cls, pokemon_type: str) -> Dict[str, float]:
        with open('type_chart.csv', 'r') as file:
            complete_csv_content = list(csv.reader(file))

        all_pokemon_types = cls.get_all_pokemon_types()
        indexes = cls.__get_indexes(all_pokemon_types, [pokemon_type])

        attack_efectiveness = (
            Matrix_Subset_Builder(complete_csv_content)
            .add_rows(*indexes)
            .delete_columns(0)
            .build_subset()
            .flatten()
            .matrix_subset
        )

        formatted = dict(zip(all_pokemon_types, attack_efectiveness))

        return formatted

    @classmethod
    def get_defense_efectiveness(cls, pokemon_types: List[str]) -> Dict[str, float]:
        with open('type_chart.csv', 'r') as file:
            complete_csv_content = list(csv.reader(file))

        all_pokemon_types = cls.get_all_pokemon_types()
        indexes = cls.__get_indexes(all_pokemon_types, pokemon_types)

        defense_efectiveness = (
            Matrix_Subset_Builder(complete_csv_content)
            .add_columns(*indexes)
            .delete_rows(0)
            .build_subset()
            .vertical_prod()
            .matrix_subset
        )

        formatted = dict(zip(all_pokemon_types, defense_efectiveness))

        return formatted

    @classmethod
    def __get_indexes(cls, all_pokemon_types: List[str], pokemon_types: List[str]) -> List[int]:
        indexes = []

        for pokemon_type in pokemon_types:
            index = all_pokemon_types.index(pokemon_type) + 1
            indexes.append(index)

        return indexes

import csv

from data_warehouse.engines import Matrix_Subset_Builder


class Type_Chart_Repository:
    @classmethod
    def get_all_pokemon_types(cls):
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
    def get_attack_efectiveness(cls, pokemon_type: str):
        with open('type_chart.csv', 'r') as file:
            complete_csv_content = list(csv.reader(file))

        all_pokemon_types = cls.get_all_pokemon_types()

        index = all_pokemon_types.index(pokemon_type)

        attack_efectiveness = (
            Matrix_Subset_Builder(complete_csv_content)
            .add_rows(index + 1)
            .delete_columns(0)
            .build_subset()
            .flatten()
            .matrix_subset
        )

        formatted = dict(zip(all_pokemon_types, attack_efectiveness))

        return formatted

    @classmethod
    def get_defensive_efectiveness(cls, pokemon_types):
        with open('type_chart.csv', 'r') as file:
            complete_csv_content = list(csv.reader(file))

        all_pokemon_types = cls.get_all_pokemon_types()

        indexes = [
            index + 1
            for index in map(all_pokemon_types.index, pokemon_types)
        ]

        defense_efectivess = (
            Matrix_Subset_Builder(complete_csv_content)
            .add_columns(*indexes)
            .delete_rows(0)
            .build_subset()
            .vertical_prod()
            .matrix_subset
        )

        formatted = dict(zip(all_pokemon_types, defense_efectivess))

        return formatted

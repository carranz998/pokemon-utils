from itertools import chain

import numpy as np


class Matrix_Subset_Builder:
    def __init__(self, matrix):
        self.matrix_subset = matrix.copy()
        self.rows_to_add = []
        self.cols_to_add = []
        self.rows_to_delete = []
        self.cols_to_delete = []

    def add_rows(self, *row_indexes):
        self.rows_to_add.extend(row_indexes)

        return self

    def add_columns(self, *col_indexes):
        self.cols_to_add.extend(col_indexes)

        return self

    def delete_rows(self, *row_indexes):
        self.rows_to_delete.extend(row_indexes)

        return self

    def delete_columns(self, *col_indexes):
        self.cols_to_delete.extend(col_indexes)

        return self

    def build_subset(self):
        new = []

        if not self.rows_to_add:
            self.rows_to_add = list(range(len(self.matrix_subset)))

        if not self.cols_to_add:
            self.cols_to_add = list(range(len(self.matrix_subset)))

        valid_rows = set(self.rows_to_add) - set(self.rows_to_delete)
        valid_columns = set(self.cols_to_add) - set(self.cols_to_delete)

        for row_index in valid_rows:
            new_row = []
            for col_index in valid_columns:
                value = self.matrix_subset[row_index][col_index]
                try:
                    new_row.append(float(value))
                except ValueError:
                    new_row.append(value)

            new.append(new_row)

        self.matrix_subset = new

        return self

    def flatten(self):
        self.matrix_subset = list(chain.from_iterable(self.matrix_subset))

        return self

    def vertical_prod(self):
        if len(self.matrix_subset[0]) > 1:
            matrix_subset = (
                np.array(self.matrix_subset, dtype=float)
                .prod(axis=1)
                .tolist()
            )

            self.matrix_subset = matrix_subset

        return self

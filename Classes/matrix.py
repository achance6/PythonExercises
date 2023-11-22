class Matrix:
    def __init__(self, matrix_string: str):
        self.rows = [[int(elem) for elem in row.split()] 
                     for row in matrix_string.split('\n')]

        self.columns = [list(col) for col in zip(*self.rows)]

    def row(self, index):
        """Returns row of internal matrix. 1-based indexing"""
        return self.rows[index - 1]

    def column(self, index):
        """Returns row of internal matrix. 1-based indexing"""
        return self.columns[index - 1]

matrix = Matrix('10 2 3\n4 5 6\n7 8 9')
print(matrix.rows)
print(matrix.columns)
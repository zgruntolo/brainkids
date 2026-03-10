class ButtonGridLayout:
    def __init__(self, frame, rows_per_column=4):
        self.frame = frame
        self.rows_per_column = rows_per_column
        self.last_columns = 0

    def reset(self):
        for c in range(self.last_columns):
            self.frame.columnconfigure(c, weight=0)

    def apply(self, num_items):
        self.reset()
        num_columns = max(
            1, (num_items + self.rows_per_column - 1) // self.rows_per_column
        )
        for c in range(num_columns):
            self.frame.columnconfigure(c, weight=1)
        self.last_columns = num_columns
        return num_columns

    def position(self, index):
        return index % self.rows_per_column, index // self.rows_per_column

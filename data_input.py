from os import path
import sys
import pandas as pd
# argv.py


class DataInput:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    supported_file_extensions = [
        '.csv',
    ]

    def change_to_lower_case(self, data):
        # change column names to lowwer case
        for column in data.columns.values:
            data.rename(columns={column: column.lower()}, inplace=True)
        return data

    def inputFunction(self):
        
        filename, file_extension = path.splitext(sys.argv[1])
        data = pd.read_csv(filename+file_extension)
        
        data = self.change_to_lower_case(data)

        return data

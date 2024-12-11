import pandas as pd

class PreProcessingClass:
    def __init__(self, MONATSZAHL, AUSPRAEGUNG, JAHR, MONAT, encoder):

        self.parent_df = pd.DataFrame({
            'MONATSZAHL': [MONATSZAHL],
            'AUSPRAEGUNG': [AUSPRAEGUNG],
            'JAHR': [JAHR],
            'MONAT': [MONAT]
        })

        self.encoder = encoder

    def _convert_date(self, column_name='MONAT', special_value='Summe'):

        day_mapping = {
            '01': 'January',
            '02': 'February',
            '03': 'March',
            '04': 'April',
            '05': 'May',
            '06': 'June',
            '07': 'July',
            '08': 'August',
            '09': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }

        data_copy = self.parent_df.copy()
        data_copy[column_name] = data_copy[column_name].apply(lambda x: day_mapping[x[4:]] if x != special_value else x)

        return data_copy

    def _one_hot(self, data):
        
        columns_to_encode = ['MONATSZAHL', 'AUSPRAEGUNG', 'JAHR', 'MONAT']

        data_copy = data.copy()

        encoded_columns = self.encoder.transform(data[columns_to_encode])

        encoded_column_names = self.encoder.get_feature_names_out(columns_to_encode)

        encoded_df = pd.DataFrame(encoded_columns, columns=encoded_column_names, index=data.index)

        final_df = pd.concat([data.drop(columns=columns_to_encode),encoded_df], axis=1)

        return final_df

    

    

    
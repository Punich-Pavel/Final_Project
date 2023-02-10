''' Инструмент создания датафрейма из Excel-книги:

            - file  - файл Excel-книги;
            - sheet - лист Excel-книги;
            - usecols - столбец листа, по умолчанию имеет значение None(по умолчанию- None(выбираются все столбцы листа))
        
        После добавления название столбца меняется на название листа

'''

import pandas as pd

def add_col(file, sheet, usecols=None):
    df = pd.read_excel(file, sheet_name=sheet,
                       usecols=usecols
                       ).rename({2020: sheet}, axis=1)
    
    return df
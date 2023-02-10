import pandas as pd
import regex as re

    
""" Инструмент исправления и удаления несуществующих (устаревших)  названий субъектов РФ 

        Описание переменных:
            - df - DataFrame;
            - region_names - словарь { регулярное выражение : название региона}; 
            - names_to_drop - позволяет сразу исключить некоторые регионы, которые могут быть ошибочно обработаны функцией как федеральные субъекты;
            - region_col - колонка DataFrame с названиями регионов."""
            
def fix_name_reg(df, region_names, names_to_drop=None, region_col='region'):        
    
    def get_reg_name(x):
        
        # Функция для .apply()  Просмотр столбца регионов и вывод названий в стандартном виде"""
    
        for key, value in region_names.items():
            x = re.sub('[\(].*?[\)]', '', x)  # удаляем спецсимволы '[\(].*?[\
            if re.search(key, x.lower()):
                return value
        return None
    
    if names_to_drop is None:
        names_to_drop = []
    df = df[~df[region_col].isin(names_to_drop)].copy()
    df[region_col] = df[region_col].apply(get_reg_name)
    
    return (df.dropna(subset=region_col).set_index(region_col).sort_index()) 
  

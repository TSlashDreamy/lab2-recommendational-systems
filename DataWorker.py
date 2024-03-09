import pandas as pd
from pandas import DataFrame
from constants import *


class DataWorker:
    def __init__(self, in_data_set: DataFrame):
        # Створення нового DataFrame для збереження рекомендацій
        self.recommendations = pd.DataFrame()
        # Зчитування даних з Excel файлу з конвертацією в стрічковий формат
        self.df = pd.read_excel(in_data_set).astype(str)
        # Зміна орієнтації DataFrame на транспоновану та встановлення стовпця "objects" як індексу
        self.df = self.df.set_index(obj_index).T
        # Запис транспонованого DataFrame у новий Excel-файл
        self.df.to_excel(transposed_data_set_name)
        # Зчитування даних з нового Excel файлу, з використанням стовпця "objects" як індексу
        self.transposedDataSet = pd.read_excel(transposed_data_set_name, index_col=0)

    def get_transposed_data(self):
        return self.transposedDataSet

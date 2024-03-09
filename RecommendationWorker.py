import pandas as pd
from pandas import DataFrame

from constants import recommendations_data_set_name


class RecommendationWorker:
    def __init__(self, transposed_data_set: DataFrame):
        # Порожній список для рекомендацій
        self.recommendationList = list()
        # Порожній DataFrame для подальшої роботи
        self.recommendationDataSet = pd.DataFrame()
        self.transposedDataSet = transposed_data_set

    def get_recommendations(self, write_to_file = False):
        print('Working on recommendations...')
        # Цикл по стовпцям (об'єктах) у DataFrame
        for row in self.transposedDataSet:
            # Виведення назви поточного об'єкта
            print(f'Working on: {row}')
            # Ініціалізація лічильника кількості схожих об'єктів
            k = 0
            # Обчислення матриці кореляції між поточним об'єктом і іншими
            corr_matr = self.transposedDataSet.corrwith(self.transposedDataSet[row])
            # Конвертація результатів у DataFrame
            corr_matr = pd.DataFrame(corr_matr)
            # Створення тимчасової матриці кореляції
            temp_matr = corr_matr

            # Вилучення рядка з кореляціями для поточного об'єкта
            temp_matr = temp_matr.drop([row], axis=0)

            # Поки кількість знайдених схожих об'єктів не дорівнює 1
            while k != 1:
                # Знаходження назви найбільш корельованого об'єкта
                name = temp_matr.idxmax().item()
                # Знаходження значення кореляції з цим об'єктом
                value = temp_matr[0][temp_matr.idxmax().item()]
                # Додавання рекомендацій до списку
                self.recommendationList.append([row, name, value])
                # Вилучення об'єкта з тимчасової матриці
                temp_matr = temp_matr.drop([temp_matr.idxmax().item()], axis=0)
                # Збільшення лічильника
                k += 1

        # Заповнюємо DataFrame для рекомендацій
        self.recommendationDataSet = pd.DataFrame(self.recommendationList, columns=['Object', 'Recommended', 'Correlation'])
        # Записуємо DataFrame у новий Excel файл, якщо користувач цього захотів
        if write_to_file:
            print(f'Writing recommendations to {recommendations_data_set_name}...')
            self.recommendationDataSet.to_excel(recommendations_data_set_name, index=False)

        return self.recommendationList, self.recommendationDataSet

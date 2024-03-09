from DataWorker import DataWorker
from RecommendationWorker import RecommendationWorker
from constants import *

# Робота з вхідними даними
New_data_worker = DataWorker(in_data_set_name)
transposed_data = New_data_worker.get_transposed_data()

# Робота з транспонованими даними та рекомендаціями
New_recommendation_worker = RecommendationWorker(transposed_data)
recommendationList, recommendationDataSet = New_recommendation_worker.get_recommendations(write_to_file=True)

# Виведення списку рекомендацій в консоль
for recommendation in recommendationList:
    print(recommendation)

# В подальшому можемо працювати з recommendationDataSet як забажаємо

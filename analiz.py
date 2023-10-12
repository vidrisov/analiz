import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузим файл Excel
file_path = "X_bp.xlsx"
data = pd.read_excel(file_path)

# Предварительная обработка данных
# Переименуем столбцы для удобства
data.columns = ["id", "Соотношение матрица-наполнитель", "Плотность кг/м3", "Модуль упругости, ГПа",
                "Количество отвердителя, м.%", "Содержание эпоксидных групп,%_2",
                "Температура вспышки, С_2", "Поверхностная плотность, г/м2",
                "Модуль упругости при растяжении, ГПа", "Прочность при растяжении, МПа",
                "Потребление смолы, г/м2"]

# 1. Статистические метрики
summary = data.describe()

# 2. Визуализация данных
data.hist(figsize=(12, 8))
plt.suptitle("Гистограммы признаков", y=1.02)
plt.show()

# 3. Анализ корреляции
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Тепловая карта корреляции")
plt.show()

print(data.describe())


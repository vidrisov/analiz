import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Создайте список всех признаков, которые не являются целевой переменной
features = ["Соотношение матрица-наполнитель", 
            "Количество отвердителя, м.%", "Содержание эпоксидных групп,%_2",
            "Температура вспышки, С_2", "Поверхностная плотность, г/м2",
            "Потребление смолы, г/м2"]

# Создайте экземпляр стандартизатора для нормализации данных
scaler = StandardScaler()

# Цикл по всем признакам
for feature in features:
    # Начало исходных графиков
    plt.figure(figsize=(12, 4))
    
    # Гистограмма до нормализации
    plt.subplot(1, 2, 1)
    plt.title(f"Распределение {feature} (до нормализации)")
    data[feature].hist()
    plt.xlabel(feature)
    
    # Нормализация признака
    data[feature] = scaler.fit_transform(data[feature].values.reshape(-1, 1))
    
    # Гистограмма после нормализации
    plt.subplot(1, 2, 2)
    plt.title(f"Распределение {feature} (после нормализации)")
    data[feature].hist()
    plt.xlabel(feature)
    
    # Вывод максимального и минимального значения
    max_value = data[feature].max()
    min_value = data[feature].min()
    print(f"{feature}: Максимальное значение = {max_value}, Минимальное значение = {min_value}")
    
    # Завершение и отображение графиков
    plt.show()

# Сохраните обновленные данные с нормализованными признаками
data.to_excel("1.xlsx", index=False)

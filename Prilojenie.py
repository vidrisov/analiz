выбор_учащегося=0 # 1 # 3
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense
# Load the Excel file
file_path = "X_bp.xlsx"
data = pd.read_excel(file_path)
# Data Preprocessing
# Rename the columns for ease of use
data.columns = ["id","Соотношение матрица-наполнитель","Плотность кг/м3","модуль упругости, ГПа","Количество отвердителя, м.%",
                "Содержание эпоксидных групп,%_2","Температура вспышки, С_2","Поверхностная плотность, г/м2",
                "Модуль упругости при растяжении ГПа","Прочность при растяжении, МПа","Потребление смолы, г/м2"]
# Split data into features (X) and target (y)
if выбор_учащегося==0:
    X = data.drop(["id","Модуль упругости при растяжении ГПа"], axis=1)  # Features
    y = data["Модуль упругости при растяжении ГПа"]  # Target
    new_data = pd.DataFrame({'Соотношение матрица-наполнитель':[1.857],'Плотность кг/м3':[2030],'модуль упругости, ГПа':[738],'Количество отвердителя, м.%':[30],
                'Содержание эпоксидных групп,%_2':[22],'Температура вспышки, С_2':[100],'Поверхностная плотность, г/м2':[210],
                'Прочность при растяжении, МПа':[3000],'Потребление смолы, г/м2':[220]})
    st='Модуль упругости при растяжении ГПа: '
else:
  if выбор_учащегося==1:
      X = data.drop(["id","МПрочность при растяжении, МПа"], axis=1)  # Features
      y = data["Прочность при растяжении, МПа"]  # Target
      new_data = pd.DataFrame({'Соотношение матрица-наполнитель':[1.857142857],'Плотность кг/м3':[2030],'модуль упругости, ГПа':[738],
                  'Количество отвердителя, м.%':[30],'Содержание эпоксидных групп,%_2':[22],'Температура вспышки, С_2':[100],
                  'Поверхностная плотность, г/м2':[210],'Модуль упругости при растяжении ГПа':[70],
                  'Потребление смолы, г/м2':[220]})
      st='Прочность при растяжении, МПа: '
  else:
    X = data.drop(columns=["id","Соотношение матрица-наполнитель"])
    y = data["Соотношение матрица-наполнитель"]
    new_data = pd.DataFrame({'Плотность кг/м3':[2030],'модуль упругости, ГПа':[738],
                'Количество отвердителя, м.%':[30],'Содержание эпоксидных групп,%_2':[22],'Температура вспышки, С_2':[100],
                'Поверхностная плотность, г/м2':[210],'Модуль упругости при растяжении ГПа':[70],
                'МПрочность при растяжении, МПа':[3000],'Потребление смолы, г/м2':[220]})
    st='Соотношение матрица-наполнитель: '

if выбор_учащегося>1:
  model = keras.Sequential()
  model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
  model.add(Dense(64, activation='relu'))
  model.add(Dense(32, activation='relu'))
  model.add(Dense(1, activation='linear'))
  model.compile(optimizer='adam', loss='mean_squared_error')
  history = model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))
else:
  # Разделение данных на обучающую и тестовую выборки
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
  # Создание модели RandomForestRegressor
  model = RandomForestRegressor(n_estimators=500, random_state=0)
  # Обучение модели на обучающих данных
  model.fit(X_train, y_train)

res = model.predict(new_data)
print(st+str(res[0]))

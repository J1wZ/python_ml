# %% [markdown]
# Домашнее задание
# по теме «AutoML алгоритмы для работы с данными»
# 
#     2. Прогнозирование временных рядов

# %%
import warnings
import seaborn as sns
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd # работа с таблицами
import numpy as np # математические вычисления
from scipy import stats # статистические методы
import matplotlib
import matplotlib.pyplot as plt # визуализация данных

from dateutil.parser import parse # парсер даты


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf # plot_acf график автокорреляции, plot_pacf частичной автокорреляции
from statsmodels.graphics.tsaplots import month_plot,quarter_plot # график сезонности данных по месяцам, кварталам
from pandas.plotting import lag_plot # график лага

from statsmodels.tsa.stattools import adfuller # тест Дики-Фуллера

from sklearn.metrics import mean_squared_error # метрика качества MSE
from statsmodels.tools.eval_measures import rmse  # метрика качества Квадратный корень из MSE
from sklearn.model_selection import train_test_split
import pycaret
from statsmodels.tsa.seasonal import seasonal_decompose

# %%
plt.rcParams["figure.figsize"] = (10,5) # размер графиков

plt.style.use('fivethirtyeight') # стиль графиков

# %%
train_df= pd.read_csv(
    "monthly-beer-production-in-austr.csv",
    index_col="Month", parse_dates= True
    )

train_df.head()

# %%
train_df.dtypes

# %%
train_df.info(memory_usage=True)

# %%
# создаем индекс (уникальность) по полю дата
train_df.index= pd.to_datetime(train_df.index)

# %%
train_df.index

# %% [markdown]
# Уменишим размер датасета

# %%
int_cols = train_df.select_dtypes('int').columns

float_cols = train_df.select_dtypes('float').columns
for col in int_cols:
    train_df[col] = pd.to_numeric(train_df[col], downcast='integer')
for col in float_cols:
    train_df[col] = pd.to_numeric(train_df[col], downcast='float')

# %%
train_df.info(memory_usage=True)

# %% [markdown]
# # EDA

# %%
train_df.describe()

# %%
#Подсчитываем сколько процентов незаполнено столбце
percent_missing = train_df.isnull().sum() * 100 / len(train_df.index)
missing_value_df = pd.DataFrame({'Незаполнено столбце %': percent_missing})

missing_value_df

# %%
#Находим медиану
median_df = pd.DataFrame({'Медиана': train_df.median()})

median_df

# %%
#Находим дисперсию
var_df = pd.DataFrame({'Диспрерсия': train_df.var()})

var_df

# %%
sns.histplot(train_df['Monthly beer production'], kde=True)
plt.title("Распределение Monthly beer production")
plt.show()

# %%
train_df.plot(
    kind='box',
    subplots=True,
    sharey=False,
)
plt.show()

# %% [markdown]
# Нет пропушенных значений в датасете. В данных нет выбросов.

# %% [markdown]
# Данные подходят для обучения модели.

# %% [markdown]
# # Анализ временного ряда

# %%
# дескриптивная аналитики, расчеты скользящего окна
train_df['12-month-SMA'] = train_df['Monthly beer production'].rolling(window=12).mean()
train_df['12-month-Std'] = train_df['Monthly beer production'].rolling(window=12).std()

train_df[['Monthly beer production','12-month-SMA','12-month-Std']].plot();

# %%
# сезонная декомпозиция
ssn= seasonal_decompose(train_df["Monthly beer production"], model="add")
fig = ssn.plot()
fig.set_size_inches((14, 10))
fig.tight_layout()
plt.show()

# %%
# построим новый вид графика
month_plot(train_df['Monthly beer production']);

# %%
# ACF
title = 'График автокорреляции'
lags = 40 # оптимальное значение (т.к. большой времнной период)
plot_acf(train_df["Monthly beer production"],title=title,lags=lags)

# %%
# PACF - функция частичной автокорреляции дает частичную корреляцию стационарного временного ряда с его собственными запаздывающими значениями
title = 'Частичная автокорреляция временных рядов'
lags = 40
plot_pacf(train_df["Monthly beer production"],title=title,lags=lags);

# %% [markdown]
# С начала 1960-х кол-во производимого пива в год постепенно увеличивалось, а в 1980-х остановилось и оставалось примерно одинаковым.
# 
# Изменение кол-ва производимого пива связано с временем года. Зимой производится больше всего пива, а летом - меньше всего. График автокорреляции поддерживает этот вывод.
# 
# PACF тоже указывает на годовую зависимость данных. Пики на 12 (декабрь) лагах, и минимумы на 6 (июнь).

# %% [markdown]
# # Cтационарность

# %%
def adf_test(series,title=''):
  '''
  тест Дики-Фуллера
  0 гипотеза: ряд данных не стационарен
  альтернативная гипотеза: ряд данных стационарен
  Понятие стационарного временного ряда означает, что его среднее значение не изменяется во времени, т. е. временной ряд не имеет тренда
  @param series - значения ряда
  @param title - заголовок ряда
  '''

  result = adfuller(series.dropna(),autolag='AIC') # тест предполагает линейный тренд

  labels = ['ADF тест','p-value','# lags used','# наблюдения']
  out = pd.Series(result[0:4],index=labels)

  for key,val in result[4].items():
      out[f'критическое значение ({key})']=val

  print(out.to_string())

  if result[1] <= 0.05:
      print("Сильные доказательства против нулевой гипотезы")
      print("Отменяем 0 гипотезу")
      print("Данные стационарны")
  else:
      print("Слабые доказательства против нулевой гипотезы")
      print("Не отменяем 0 гипотезу")
      print("Данные не стационарны")

# %%
# тест на стационарность, p-value < 0.05
adf_test(train_df["Monthly beer production"])

# %% [markdown]
# # AutoML

# %%
my_random_state = 42

# %%
train = train_df[:round(len(train_df)*0.8)].copy()
test= train_df.iloc[round(len(train_df)*0.8):].copy()

# %%
from pycaret.time_series import *
s = setup(train, fh = 10, fold = 5, session_id = my_random_state)

# %%
best = s.compare_models()

# %% [markdown]
# Лучшая модель для прогнозирования:

# %%
best

# %%
s.plot_model(best, plot = 'forecast', data_kwargs = {'fh' : 24})

# %% [markdown]
# Подберем лучшие гиперпараметры

# %%
tuned = tune_model(best) # настройка гиперпараметров

# %%
tuned

# %%
s.plot_model(tuned, plot = 'forecast', data_kwargs = {'fh' : 24})

# %%
len(test)

# %% [markdown]
# Спрогнозируем 95 шагов вперед, так как это длина наших данных для теста.

# %%
forecast = predict_model(tuned, fh = 95)

# %%
plt.figure(figsize=[30, 8])
plt.plot(forecast.index.strftime('%Y-%m'), forecast['y_pred'].astype(float),label = 'forecast')
plt.plot(test.index.strftime('%Y-%m'),test['Monthly beer production'].astype(float),label = 'test')
plt.legend(loc=[1,1])
plt.xticks(rotation=45)

# %%
from sklearn.metrics import mean_squared_error, root_mean_squared_error
from sklearn.metrics import mean_absolute_error, r2_score

err_dict = {}

err_dict['AutoMl'] = {'Mean Absolute Error' : mean_absolute_error(test,forecast),
                      'Mean Squared Error' : mean_squared_error(test,forecast),
                      'Root Mean Squared Error' : root_mean_squared_error(test,forecast),
                      'r2' : r2_score(test,forecast),}
err_dict

# %%
finalModel = finalize_model(tuned)
save_model(finalModel, 'bestModel')

# %% [markdown]
# Для сравнения обучим HuberRegressor без AutoML

# %% [markdown]
# # HuberRegressor

# %%
from sklearn.linear_model import HuberRegressor

df = train.copy()
df['lag_1'] = train['Monthly beer production'].shift(1)
df['lag_2'] = train['Monthly beer production'].shift(2)
df.dropna(inplace=True)

X = df[['lag_1', 'lag_2']]
y = df['Monthly beer production']

model = HuberRegressor ()
model.fit(X, y)

y_pred = model.predict(X)

# %%
len(y_pred)

# %%
len(test)

# %%
y_pred_series = pd.Series(y_pred[:95], index=test.loc[:, ['Monthly beer production']].index)
y_pred_series

# %%
ax = test.loc[:, 'Monthly beer production'].plot()
ax = y_pred_series.plot(ax=ax, linewidth=3)
ax.set_title('Time Plot of Tunnel Traffic');

# %%
err_dict['HuberRegressor'] = {'Mean Absolute Error' : mean_absolute_error(test["Monthly beer production"],y_pred_series),
                      'Mean Squared Error' : mean_squared_error(test["Monthly beer production"],y_pred_series),
                      'Root Mean Squared Error' : root_mean_squared_error(test["Monthly beer production"],y_pred_series),
                      'r2' : r2_score(test["Monthly beer production"],y_pred_series),}

# %%
pd.DataFrame(err_dict)

# %% [markdown]
# HuberRegressor без AutoML показала результаты хуже.



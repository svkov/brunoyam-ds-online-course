# Урок 3. Библиотека pandas

## Библиотека pandas

Библиотека `pandas` позволяет удобно работать с табличными данными. Во многих задачах `pandas` позволяет заменить Excel, предоставляя возможность легко фильтровать, сортировать и агрегировать данные.

Также `pandas` позволяет читать файлы с табличными данными и записывать таблицы в файлы в разных форматах. Самый простой формат файлов, с которым мы будем работать - CSV (comma separated values). По сути, это обычный текстовый файл, в котором значения разделены разделителем (обычно это точка или точка с запятой), а перенос на новую строку означает начало новой строки.

Установить `pandas` можно при помощи `conda` и `pip`:

`conda install pandas`

`pip install pandas`

## Поработаем с данными

Для начала давайте импортируем библиотеку:

```python3
import pandas as pd
```

Как и в случае с `numpy`, в `pandas` есть общепринятое сокращение - `pd`.

### Series

Самая простая структура в `pandas` - `Series`. По сути, серия - столбец в таблице (ну или массив/вектор).

```python3
series = pd.Series([1, 2, 3])
print(series)

# Выведет:
0    1
1    2
2    3
dtype: int64
```

Серия также хранит индекс (левый столбец). Индекс сопоставляет каждому значению серии какое-то число. Также индекс может быть, например, датой, и тогда мы сможем понять в какой день проводилось измерение.

```python3
series.index # RangeIndex(start=0, stop=3, step=1)

series.values # array([1, 2, 3])
```

Также индекс может быть строкой и его можно указать при создании серии:

```python3

legs_counter = pd.Series([4, 4, 8], index=["cat", "dog", "spider"])
print(legs_counter)

# Выведет:
cat       4
dog       4
spider    8
dtype: int64
```

По series можно индексирования при помощи loc и iloc

- loc - если хотим взять по индексу
- iloc - если хотим взять по порядковому номеру

```python3
legs_counter.iloc[2] # 8
```

```python3
legs_counter.loc["dog"] # 4
```

### DataFrame

Датафрейм - основная структура `pandas` и она позволяет работать с таблицами. Каждый столбец таблицы является серией, а также есть "главная" колонка - индекс - по которой можно легко искать нужные значения:

```python3
ages = [25, 35, 45]
heights = [170, 180, 190]
names = ["Alex", "Polina", "Misha"]
data = {'age': ages, 'height': heights, 'name': names}
df = pd.DataFrame(data)
print(df)

# Выведет:
    age height  name
0   25  170     Alex
1   35  180     Polina
2   45  190     Misha
```

Поработаем с датафреймом:

```python3
df['age'] # Получился Series
0    25
1    35
2    45
Name: age, dtype: int64


df[['age', 'height']] #Получился DataFrame
    age height
0   25  170
1   35  180
2   45  190

df[['age']] # Получился DataFrame
    age
0   25
1   35
2   45

# Можно добавить новую колонку
df['height/age'] = df['height'] / df['age']
age height  name    height/age
0   25  170 Alex    6.800000
1   35  180 Polina  5.142857
2   45  190 Misha   4.222222

# Можем посчитать суммы/минимумы/максимумы/средние значения
df["age"].sum()
df["age"].min()
df["age"].max()
df["age"].mean()
```

Датафреймы можно фильтровать. Но нужно быть внимательным, ведь сам датафрейм не изменится из-за фильтрации, поэтому нужно складывать результат в новую переменную, если захотим его использовать в дальнейшем.

```python3
df[df['age'] == 25] # Обратите внимание, что сам датафрейм не изменился

    age height  name    height/age
0   25  170     Alex    6.8


df[(df['age'] > 35) & (df['height'] > 170)]

    age height  name    height/age
2   45  190     Misha   4.222222
```

Если нужно поменять какое-то значение, можно использовать .loc

```python3
df.loc[df['age'] == 25, 'age'] = 20

# Проверим, что датафрейм изменился
df[df['height/age'] > 5]
    age height  name    height/age
0   20  170     Alex    6.800000
1   35  180     Polina  5.142857
```

При помощи `apply` мы можем создавать новые колонки из уже имеющихся. Например, если мы хотим поделить людей на "низких" и "высоких" по какому-то порогу, то нужно сделать функцию, которая на вход будет принимать рост, а на выходе скажет высокий человек или низкий. Далее эту функцию нужно передать в `apply`.

```python3
df["height_category"] = df["height"].apply(lambda x: "высокий" if x > 175 else "низкий")

    age height  name    height/age  height_category
0   20  170 Alex    6.800000    низкий
1   35  180 Polina  5.142857    высокий
2   45  190 Misha   4.222222    высокий
```

## Работаем с пропусками

Некоторые данные в таблицах могут быть пропущены. Пропуски надо как-то обрабатывать: либо заполнять, либо убирать.

```python3
values = [[None, 1, 2], [None, 2, 3], [None, None, 4]]
df = pd.DataFrame(values, columns=["a", "b", "c"])
print(df)

# Результат:
    a       b   c
0   None    1.0 2
1   None    2.0 3
2   None    NaN 4
```

Чтобы удалить пропуски, существует функция `dropna()`

У dropna есть два важных аргумента:

- axis (по-умолчанию 0) - по строкам или по колонкам будем искать наны
- how (по-умолчанию 'any') - бывает any и all, ниже пример использования
Удалим столбец a, потому что в нем все (all) значения None

```python3
dropped_a = df.dropna(axis=1, how='all')
print(dropped_a)

    b   c
0   1.0 2
1   2.0 3
2   NaN 4
```

В последней строке есть один None. Нам это не подходит, удалим его:

```python3
dropped_a.dropna(axis=0, how='any')

    b   c
0   1.0 2
1   2.0 3
```

Критично ли будет, что мы удалим какой-то объем данных? Зависит от задачи. Если у вас 5 миллионов изображений и вы удалите 4 миллиона поврежденных изображений, то это не страшно, ведь все еще остается миллион картинок. С другой стороны, если вы получили данные о 30 дорогостоящих экспериментах и 5 из них некачественные, то стоит приложить усилия, чтобы как-то искусственно восстановить результаты. Обычно если при очистке данных удаляется около 30%, то это нормальный результат.

Альтернативой удалению пропусков может быть заполнение пропусков. За это отвечает функция `fillna()`. Есть несколько способов заполнения пропусков:

- Заполнение каким-то числом (средним значением или 0, например)
- Forward-fill (ffill) - заполнение пропуска последним не-None значением
- Back-fill (bfill) - заполнение пропуска следующим не-None значением

```python3
df.fillna(0)

    a   b   c
0   0   1.0 2
1   0   2.0 3
2   0   0.0 4

# Тоже самое, что и df.ffill()
df.fillna(method="ffill")
# Заполнился столбец b

    a       b   c
0   None    1.0 2
1   None    2.0 3
2   None    2.0 4
```

Когда каким методом пользоваться - зависит от ситуации и логики в данных.

Если у вас есть данные о погоде и за какой-то час наблюдения отсутствуют, то можно воспользоваться `ffill`, так как температура редко значительно изменяется за час.

Если вы работаете с данными по объемам поставок и за какой-то промежуток у вас нет данных и вы знаете, что это равносильно отсутствию поставок, тогда можно заполнить пропуски нулями.

## Работаем с данными

Давайте прочитаем файл с погодой [`weather.csv` из репозитория](https://github.com/svkov/brunoyam-ds-online-notebooks/blob/main/data/weather.csv) (для этого необходимо загрузить себе либо этот файл, либо весь репозиторий) при помощи функции `pd.read_csv`. Аргументов в функцию нужно передать путь до файла. В примере ниже предполагается, что файл лежит в папке data.

Данных довольно много, поэтому давайте посмотрим на первые 5 записей при помощи функции `head()`.

```python3
df = pd.read_csv('data/weather.csv`)
df.head()

    Day         t
0   2008-01-01  0
1   2008-01-02  -5
2   2008-01-03  -11
3   2008-01-04  -11
4   2008-01-05  -12
```

Видим, что в данных всего две колонки - день измерения температуры и среднесуточная температура. Обычно при работе с датой номера месяца, года и дня записывают в отдельные колонки, давайте сделаем также.

При помощи функции `pd.to_datetime` можно привести series к типу datetime. Функция довольно умная и сама понимает несколько форматов дат, но если на каких-то данных сработает неверно, то можно [посмотреть документацию](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) и задать нужные параметры, чтобы дата стала верной.

```python3
# Приводим колонку к типу datetime
df["Day"] = pd.to_datetime(df["Day"])

# Создаем новые колонки
df["year"] = df.Day.dt.year
df["month"] = df.Day.dt.month
df["day"] = df.Day.dt.day

# Выведем результат
df.head()

    Day         t   year    month   day
0   2008-01-01  0   2008    1       1
1   2008-01-02  -5  2008    1       2
2   2008-01-03  -11 2008    1       3
3   2008-01-04  -11 2008    1       4
4   2008-01-05  -12 2008    1       5
```

Чтобы записать датафрейм в csv файл можно использовать функцию `pd.to_csv()` и передать путь:

```python3
df.to_csv('data/new_weather.csv')
```

Также pandas умеет работать с различными другими форматами: [Excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html), [JSON](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html), [XML](https://pandas.pydata.org/docs/reference/api/pandas.read_xml.html), [HDF](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html), а также умеет подключаться к базам данных и брать данные прямо оттуда. О том как работать с базами данных мы поговорим на следующем уроке.

## Группировка и агрегация данных

Иногда нужно объединять строки, в которых есть какие-то одинаковые значения.

Например, мы хотим посчитать среднюю температуру для каждого месяца. Это значит, что нам нужны строки, в которых совпадают year и month

```python3
df.groupby(["year", "month"]).mean()

            t           day
year    month
2008    1   -1.612903   16.000000
        2   0.034483    15.000000
        3   1.516129    16.000000
        4   9.566667    15.500000
        5   14.133333   16.333333
...     ... ...         ...
2016    8   19.161290   16.000000
        9   14.366667   15.500000
        10  5.870968    16.000000
        11  -1.433333   15.500000
        12  -0.806452   16.000000
```

Вопрос на подумать: почему среднее по дням разное?

Иногда мы хотим применить какую-то функцию, которой нет в стандартном pandas или хотим применить много разных функций к определенным строкам. Для этого существует метод agg (сокращение от Aggregate)

```python3
df.groupby(["month"]).agg(['mean', 'max', 'std']) # Применяем много функций ко всем столбцам

    t                           year                            day
    mean        max std         mean        max     std         mean        max std
month
1   -5.745520   5   6.316853    2012.000000 2016    2.586629    16.000000   31  8.960344
2   -3.505882   6   5.953805    2012.000000 2016    2.596181    14.670588   29  8.196967
3   0.759857    13  4.252342    2012.000000 2016    2.586629    16.000000   31  8.960344
4   7.744444    21  4.167214    2012.000000 2016    2.586784    15.500000   30  8.671515
5   15.291367   30  5.149533    2012.014388 2016    2.580084    16.035971   31  8.956300
... ...         ... ...         ...         ...     ...         ...         ... ...
```

Еще один пример:

```python3
df.groupby(["month"]).agg(
    {'t':[
        ('one',  np.mean), 
        ('two', lambda value: 100 * ((value>32).sum() / value.std())), 
        ('three', lambda value: 100* ((value > 45).sum() / value.mean()))
    ]}
)

                            t
    one         two         three
month
1   -5.745520   0.000000    -0.0
2   -3.505882   0.000000    -0.0
3   0.759857    0.000000    0.0
4   7.744444    0.000000    0.0
5   15.291367   0.000000    0.0
```

## Что дальше?

Pandas - очень большая библиотека и выше было описание лишь небольшого количества ее функционала. Чем дольше вы будете с ней работать, тем больше будете про нее узнавать. Но чтобы облегчить ваш путь, ниже приводим набор ссылок по полезным функциям, которые делают довольно специфичные операции над данными. Они используются довольно редко, но иногда задача сильно облегчается, если использовать их. Приводим материалы на документацию pandas (первоисточник), при необходимости можно найти эти же материалы и на руссском языке.

- [Multiindex](https://pandas.pydata.org/docs/user_guide/advanced.html)
- [Melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
- [Pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
- [Explode](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html)
- [Stack](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html) & [Unstack](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html)
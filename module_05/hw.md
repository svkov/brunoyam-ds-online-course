# Домашняя работа

Перед решением домашней работы рекомендуется посмотреть [второй](https://github.com/svkov/brunoyam-ds-online-notebooks/blob/main/notebooks/02-pandas-numpy-matplotlib.ipynb) и [третий](https://github.com/svkov/brunoyam-ds-online-notebooks/blob/main/notebooks/03-advanced_pandas-matplotlib.ipynb) ноутбук в репозитории на GitHub и решить задачи оттуда. Это необязательно, но точно поможет набить руку на более простых задачах.

## Easy

Скачать данные отсюда (кнопка download all снизу):

<https://www.kaggle.com/c/titanic/data>

Это данные о пассажирах Титаника и информация о том, кто выжил, а кто нет. Будем анализировать файл train.csv.

Необходимо прочитать файл, посчитать процент детей (младше 18 лет), соотношение мужчин/женщин на борту

## Normal

Посчитать по скольким людям нет информации (пола или возраста)

Вывести гистограмму по возрасту пассажиров

Посчитать какой процент мужин и женщин выжили, какой процент детей выжили.

## Hard

Сделав вывод по данным, написать простейшую модель, которая будет определять по входным данным, выжил ли человек. Проверить свою гипотезу на данных train.csv, оценить успешность модели. Прогнать модель на файле test.csv

Загрузить решение на kaggle.

Решение представляет из себя файл с 2 колонками: PassengerId и Survived. Id пассажиров и их данные нужно брать из файла test.csv.
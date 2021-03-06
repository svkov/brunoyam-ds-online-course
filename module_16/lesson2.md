# Инструменты для построения конвейеров

## Обзор инструментов

Для построения конвейеров существует множество инструментов. Что вообще должен в себе содержать такой инструмент? Во-первых, он должен позволять как-то организовывать очередность запуска кода. Например, мы должны как-то указать, что сначала мы будем запускать загрузку данных и их обработку, а потом будем строить модели и сохранять картинки графиков. Во-вторых, такой инструмент должен уметь работать распределенно на нескольких машинах или процессорах. Некоторые задачи можно делать параллельно, и инструмент должен сам это понимать и запускать. В-третьих, результаты должны быть воспроизводимы. Два запуска конвейера должны давать один и тот же результат при работе с одним и тем же кодом.

Самый известный инструмент - Airflow. Он имеет множество функций, но его довольно сложно установить и настроить, поэтому мы будем работать с Snakemake. Разобравшись со Snakemake, перейти на Airflow не составит труда, так как общие принципы останутся теми же.

## Введение в Snakemake

Snakemake - библиотека, позволяющая при помощи **правил** (rule) преобразовывать одни файлы в другие.

Правило принимает входные файлы (input) и при помощи скрипта формирует выходные файлы (output). Правила оформляются в файле Snakefile. Давайте посмотрим на простой пример:

```python
rule example:
    input:
        "raw_data.csv"
    output:
        "preprocessed/preprocessed.csv"
    shell:
        "python preprocess.py {input} {output}"
```

Правило позволяется сгенерировать файл `preprocessed.csv` из файла `raw_data.csv` при помощи запуска python скрипта. В скрипте может быть любой код, который читает аргументы из командной строки (пример посмотрим позже), и который генерирует выходной файл по нужному пути. Если входного файла `raw_data.csv` не будет существовать, то snakemake попытается найти правило, которое генерирует этот файл и запустит сначала его, а потом правило example. Напишем правило, которое будет скачивать данные:

```python
rule download_data:
    output:
        "raw_data.csv"
    shell:
        "python download.py {output}"
```

В скрипте download точно также может лежать любой код, который генерирует файл по нужному пути. При этом если удалить файл `preprocessed.csv`, и заново запустить snakemake, то файл `raw_data.csv` повторно скачиваться не будет, так как он уже существует.

Для того, чтобы понять в каком порядке запускать правила, snakemake строит ациклический граф работ (DAG). Начиная от файла, который запрашивался изначально, строится цепочка правил, которые генерируют все необходимые данные. Этот граф можно отобразить на картинке.

![snakemake_dag](../images/snakemake_dag.svg)

Чтобы построить такой граф, сначала ищутся все необходимые файлы на компьютере, и если какие-то из них не были найдены, то для их построения ищутся соответствующие правила.

Еще одна важная функция snakemake - это wildcards. Что бы мы делали, если бы нам нужно было предобработать не один файл, а сразу несколько? Вызвать в цикле правило не получится, но можно написать правило обобщенно.

```python
rule wildcard_example:
    input:
        "{data}.csv"
    output:
        "preprocessed/{data}.csv"
    shell:
        "python preprocess.py {input} {output}"
```

Само по себе это правило не будет делать ничего, так как вместо конкретных путей мы задали шаблон `data`, в который можно подставить любое значение. Давайте сделаем правило, которое будет генерировать 5 файлов. В файлах snakemake можно писать код на python, давайте будем использовать это.

```python
filenames = ['1', '2', '3', '4', '5']

rule call_wildcard_example:
    output:
        expand("preprocessed/{data}.csv", data=filenames)

```

В этом правиле мы просто запросили сгенерировать файлы `preprocessed/1.csv`, ..., `preprocessed/5.csv`. При помощи функции expand можно подставлять по очереди все значения из списка. В первом аргументе мы передаем строку с wildcard `data` (название могло быть другим), и далее мы передаем именованный аргумент с таким же названием.

Обычно создают правило `all`, в котором перечисляют финальные файлы, которые должны быть сгенерированы конвейером. В нашем случае правило `call_wildcard_example` как раз является таким.

## Snakemake в DS исследованиях

Вид конкретного Snakefile зависит от решаемой задачи, но обычно есть общие шаги, которые есть в каждой задаче:

1. Загрузка данных. Если данные лежат в каком-то хранилище (S3/FTP-сервер/любое облако) или достаются через API, то лучше автоматизировать загрузку оттуда. Это позволит упростить и синхронизировать работу между всеми участниками. Если данные хранятся только локально и вы работаете над проектом в одиночку, то этот шаг можно опустить.

2. Обработка данных. Сырые данные обычно содержат пропуски, неиспользуемые поля или не агрегированы. Нужно провести всю необходимую обработку и сохранить результат.

3. Подготовка датасета. Если вам нужно использовать one-hot encoding для категориальных признаков, нормализацию данных или удаление выбросов, то это стоит сделать на этом этапе. Подготовленный датасет - это таблица, которую можно прочитать и сразу отдать на обучение модели. На этом же этапе можно разделить выборку на тренировочную и тестовую, либо подготовить для кросс-валидации.

4. Обучение моделей, построение прогнозов. На этом шаге обучаются все необходимые модели, и, если это возможно, то они сохраняются в файлы. Далее по этим моделям строятся прогнозы. В случае, когда нельзя сохранить модель в файл, прогнозы строятся сразу и также сохраняются в отдельные файлы.

5. Построение графиков, подсчет метрик. Получив все прогнозы, можно построить таблицы с результатами моделей, а также все необходимые графики. После этого реализации этого шага можно начинать экспериментировать с параметрами моделей. Если конвейер построен правильно, то можно построить модель, посмотреть ее параметры, затем что-то изменить (предобработку данных, гиперпараметр модели и т.д.) и запустить заново. Уже на этом этапе можно ощутить насколько удобнее использовать конвейеры, чем просто jupyter ноутбуки.

6. Формирование отчета. В конце исследования всегда пишется отчет о проведенной работе, где подробно описываются все проведенные эксперименты. Если писать такой отчет в конце работы, то он получится неточным и с ошибками, поэтому хорошей практикой было бы писать его по ходу проекта. Каждая глобальная задача в проекте должна быть описана и задокументирована, чтобы в будущем было понятно как ее можно доработать и почему принимались те или иные решения. При помощи скриптов можно вставлять в отчет картинки и таблицы, которые будут обновляться после каждого перезапуска конвейера. Если оформлять такой отчет в формате markdown или latex, то затем его можно легко конвертировать в pdf-файл. Но даже без этого шага собрать отчет из готовых картинок и таблиц будет гораздо проще, чем совсем без конвейера.

Итак, если правильно выстроить конвейер, то проведение всего эксперимента от скачивания данных до формирования отчета можно провести запуском одной команды. Такой подход позволяет построить систему, в которой вычисления будут воспроизводимы по-крайней мере в рамках одного репозитория и одного окружения.

Если оформлять код в jupyter ноутбуках, то построить воспроизводимую систему будет гораздо сложнее. [Есть презентация](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/mobilepresent?slide=id.g362da58057_0_1), в которой приводятся примеры, почему jupyter плох для построения таких систем. Использовать jupyter для того, чтобы посмотреть на данные и написать первоначальный код - это нормально, но затем этот код должен быть перенесен в скрипты.

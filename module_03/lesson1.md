# Циклы

Программирование существует для того, чтобы упрощать жизнь себе и окружающим и автоматизировать какие-то рутинные процессы.

В то же время процесс написания кода тоже может стать рутиной. Возьмем простую задачу - вывести на экран числа от 1 до 10. Решение очевидное и простое:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
```

Однако писать такие конструкции довольно скучно и неудобно. А что делать, если нужно вывести числа от 1 до 100? от 1 до 1 000 000? Вот бы был какой-то инструмент, который делал это сам...

## Цикл while

Встречайте! Цикл while:

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

Синтаксис очень простой. После `while` нужно указать какое-то условие, которое будет проверяться перед каждый шагом цикла. В нашем случае мы завели отдельную переменную `i`, которую для контроля за циклом. Изначально мы установили `i` равное 1, и затем на каждом шаге увеличивали значение на единицу.

Можем подробно посмотреть на то как работал цикл while:

- i = 1; 1 <= 10, заходим в цикл;
- i = 2; 2 <= 10; заходим в цикл;
- ...
- i = 9; 9 <= 10; заходим в цикл;
- i = 10; 10 <= 10; заходим в цикл;
- i = 11; 11 > 10; не заходим в цикл;

Попробуйте поменять код так, чтобы выводились квадраты чисел от 1 до 10. А теперь сделать так, чтобы они выводились в обратном порядке.

С помощью цикла while можно решить любую задачу на циклы, но у них есть и недостаток. Если написать код неправильно, то можно уйти в бесконечный цикл:

```python
i = 1
while i <= 10:
    print(i)
```

Что выведет код?

Он будет печатать 1 бесконечно. Так произошло потому что мы убрали увеличение счетчика на каждом шаге и из-за этого условие всегда истинно. Если ваша программа содержит цикл while и работает слишком долго, проверьте, не возникает ли бесконечный цикл.

Кстати, переменную `i` почти всегда используют, когда нужна переменная-счетчик для цикла. Если есть два вложенных цикла, то используют переменные `i`, `j`, а в случае трех циклов еще добавляют переменную `k`.

Также добавим немного терминов:

- **тело цикла** - все, что происходит на каждом шаге цикла (после проверки условия)
- **итерация** - одно полное выполнение тела цикла

## Цикл for

Цикл `for` является более распространенным видом циклов, но некоторые задачи при помощи него решить нельзя.

Решим задачу с выводом чисел от 1 до 10 при помощи `for`:

```python
for i in range(1, 11):
    print(i)
```

Давайте разбираться, что произошло.

Мы указали переменную `i` как счетчик. Опять. Но на этот раз мы не создаем переменную самостоятельно, мы лишь говорим циклу какую переменную мы хотели бы использовать. Цикл сам будет обновлять `i` на каждом шаге цикла.

Как цикл понимает с какого значения нужно начать и каким закончить? В этом ему помогает функция `range`. Функция range говорит от какого числа нужно начать и каким закончить (причем конечное число не включается).

Например, если записать так: `range(10, 15)`, то переменная будет принимать поочередно значения `10, 11, 12, 13, 14`, после чего цикл закончится.

Если нужно пройти по числам в обратном направлении, то можно использовать третий аргумент `range`, который отвечает за величину шага по окончанию каждой итерации:

```python
for i in range(5, 0, -1):
    print(i, end=', ')
# 5, 4, 3, 2, 1, 
```

В общем виде range записывают так: `range(start, stop, step)`.

Если бы мы хотели записать цикл `for` используя цикл while, то это бы выглядело примерно так:

```python
i = start 
while start < stop: # строгий знак, последнее значение не включается
    # тело цикла
    ...
    i += step # если step отрицательный, то уменьшаем i
```

Для большинства задач цикла for бывает достаточно. А еще при помощи цикла for очень удобно работать с коллекциями, о которых мы поговорим в следующем уроке.

`for` не умеет уходить в бесконечный цикл, так как еще до старта известно сколько итераций нужно сделать.

## Continue

Задача - вывести все числа от 1 до 10, кроме 5.

Попробуйте написать свое решение, а затем сравните с решением ниже.

```python
for i in range(1, 11):
    if i != 5:
        print(i)
```

Основное тело цикла находится внутри if, если бы таких условий было несколько, это было бы некрасиво. В таких случаях хочется сначала проверить все исключительные ситуации, и закончить итерацию досрочно, если мы попали в них. Ровно это и позволяет сделать `continue`:

```python
for i in range(1, 11):
    if i == 5:
        continue

    print(i)
```

Мы пропустим только ту итерацию, где `i` примет значение 5.

## Break

Давайте посмотрим на такую задачу - даны числа `a` и `b`, нужно проверить, есть ли между ними числа, которые делятся на 5, и если да, то нужно вывести первое такое число.

Попробуйте решить самостоятельно. Подсказка: можно использовать логическую переменную-флаг, чтобы отследить, встретилось ли нам уже нужно число.

Давайте посмотрим как эта задача решается при помощи `break`. `break` позволяет прервать выполнение цикла.

```python
for i in range(a + 1, b): # Берем числа между a и b
    if i % 5 == 0: # Проверяем, делится ли на 5
        print(i) # Если да, то выводим число
        break # И выходим из цикла
```

`break` позволяет не делать лишних итераций и упрощает код.

И `continue` и `break` можно использовать в обоих циклах - `for` и `while`.

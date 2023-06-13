# Видео 2

В этом уроке мы разберемся с основными коллекциями - списками, кортежами и словарями. Чтобы понять, что это такое, давайте опять вспомним, что программисты ленивые и любят все автоматизировать. Часто нам нужно применять какую-то операцию не к одному значению, а по очереди к значениям из какого-то списка. При помощи коллекций мы можем удобно хранить разные данные и обходить их при помощи циклов.

## Списки

Для начала давайте посмотрим как работают списки. Список - это набор значений, который можно положить в одну переменную. Чтобы задать список, можно использовать квадратные скобки

```python
a = [1, 2, 3, 4, 5]

a[0]

a.append(0)
a.remove(2)
a.pop(0)
a.sort()
sorted(a)
sum(a)
len(a)

a + [3, 2, 1]
```

Что делать, если мы хотим обрабатывать каждый элемент списка каким-то похожим образом? Обойти список циклом. Есть три способа.

```python
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

for i, v in enumerate(a):
    print(i, v)
```

Списки стоит использовать, когда вы хотите хранить какие-то однотипные данные - числа, строки, логические значения. Если вы хотите сохранить значения разных типов, то питон даст вам это сделать, но вы наверняка столкнетесь с ошибкой при обработке. В этом особенность динамической типизации - она настолько гибкая, что это становится проблемой.

```python
a = [1, '2', True]

for i in a:
    print(i + 1) # Ошибка!
```

## Кортежи

Списками очень удобно пользоваться, но есть одна проблема - списки изменяемы. Мы можем присвоить новое значение любому элементу списка. Может возникнуть резонный вопрос - почему это проблема? Дело в том, что часто мы не хотим, чтобы наши данные менялись. Допустим, у нас есть отсортированный список значений, мы можем поменять любое значение и список станет не отсортированным.

```python
sorted_list = [0, 5, 10]
sorted_list[0] = 100
```

Список может поменяться, а мы этого не заметим, особенно если наша программа большая и состоит из множества файлов, связанных между собой. Также значения в вашем списке могут поменяться какой-нибудь функцией из внешней библиотеки, которую вы используете. Обычно про такие вещи пишут в документации, но это легко пропустить. Из-за этого может происходить много неочевидных багов.

Если вам важно, чтобы даже теоретически было невозможно поменять значения, заданные единожды - вам нужно использовать кортеж. Кортеж - это "замороженный" список. То есть, мы один раз его создали и потом можем только прочитать оттуда значения. Такая структура данных занимает немного меньше памяти и немного быстрее работает, это тоже можно использовать. Если же вам понадобилось добавить значение в кортеж, то можно создать новый, передав в него все значения старого кортежа и добавив еще одно.

```python
b = tuple(a)
b = (3, 2, 1)
b = (1,)
b[0]
len(b)

b[1] = 5

b.sort()
sorted(b)

for i in b:
    print(i)

b = (b[0], b[1], b[2], 10)
b = (*b, 5)

a = 1
b = 2
a, b = b, a
```

Кортежи используются не очень часто, но правильное их использование позволяет избегать досадных багов и упрощает жизнь. А еще они активно используются внутри самого питона.

## Словари

Последняя коллекция, с которой мы сегодня познакомимся - словари. Словари кардинально отличаются от списков и кортежей и позволяют реализовывать интересную логику. Как следует из названия словарь умеет как бы "переводить" одну информацию в другую. Например, можно составить словарь, который переводит слова с русского на английский.

```python
c = {
    'яблоко': 'apple',
    'червяк': 'worm'
}
c['яблоко']
c.get('яблоко', '')

c['книга'] = 'book'

c[1] = 'one'
c['one'] = 1

len(c)

for k, v in c.items():
    print(k, v)

list(c.keys())
list(c.values())
```

Говорят, что словарь умеет хранить информацию в виде ключ-значение. Как это можно использовать?

Давайте представим, что мы пишем сайт, а именно, пишем модуль, который запоминает какие пользователи заходили к нам на сайт и сколько времени в секундах они провели на странице. Сейчас мы прочитаем имя и продолжительность сессии из инпута, но при встраивании в сайт не будет никаких проблем вместо инпута подставить чтение из какого-то внешнего источника.

```python
sessions = {}

name = input()
session_len = float(input())
sessions[name] = session_len

# вариант с ифом не перезаписывая
if name in sessions:
    sessions[name] += session_len
else:
    sessions[name] = session_len

# не перезаписывая
sessions[name] = sessions.get(name, 0) + session_len
```

Как посчитать сколько суммарно времени провели пользователи на нашем сайте?

```python
sum_ = 0
for v in sessions.values():
    sum_ += v
print(sum_)
```

Также в качестве ключа словарю можно передавать не только строки и числа, но и, например, кортежи. Для примера выше мы можем запоминать не только имя пользователя, но и его айпи адресс.

```python
sessions = {}

name = input()
ip = input()
session_len = float(input())
sessions[(name, ip)] = session_len
```

Важно - в качестве ключа нельзя использовать изменяемые объекты, такие как листы и словари. Кортежи можно.

А вот значение может быть вообще любым. Если бы мы хотели записывать по отдельности каждую пользовательскую сессию, то мы бы могли сделать это так

```python
sessions = {}

name = input()
session_len = float(input())

sessions[name] = sessions.get(name, []) + [session_len]
```
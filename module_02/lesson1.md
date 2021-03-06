# Переменные и типы данных

Начнем наше знакомство с Python с того как мы можем сохранять и обрабатывать разные типы информации.

В жизни мы умеем работать с разными видами информации - звук, изображение, осязание, обоняние и вкус. Мы понимаем какая информация относится к какому типу из-за того, что мы получаем ее от разных органов.

В компьютере все устроено намного проще - любая информация представляется в виде нулей и единиц, но нам нужно как-то знать, что вот эта последовательность бит отвечает за число, а вот эта за символ. Для этого существуют типы данных.

В Python существует множество стандартных типов данных. Давайте познакомимся с основными.

## Целые числа

Целые числа - это числа без дробной части. Могут быть отрицательными и положительными (и, конечно, включают 0).

В Python носят название `int` (от англ integer - целое число).

Если у вас был опыт программирования на других языках, то вы могли слышать о том, что целые числа можно сохранять только в некотором диапазоне (обычно примерно от -2 миллиардов до 2 миллиардов), но в Python мы можем хранить целые числа любого размера.

## Вещественные числа

Вещественные числа (или числа с плавающей точкой) - это числа, которые могут содержать дробь. Точность вычислений около 16 знаков после запятой, этого достаточно для большинства задач.

В Python этот тип данных носит название `float`.

`float` ограничен в значениях, в отличие от `int`. Максимальное значение составляет примерно $10^{308}$, чего также хватает для большинства задач. Однако чем больше число, тем меньше будет его точность. Если вам не нужно хранить очень большие или очень маленькие числа, то можно не думать об этом.

Числа типа `float` и `int` можно конвертировать друг в друга:

```python
# int просто конвертируется в float
float(1) # 1.0

# float конвертируется в int, но дробная часть отбрасывается
int(1.2) # 1
int(1.8) # 1

# если нужно воспользоваться округлением, есть функция round
round(1.5) # 2
```

## Строки

Если нужно хранить строковую информацию, то для этого подойдет тип `str` (от английского string - строка). Строка - это набор символов.

Как хранятся символы? Точно также как и числа - при помощи нулей и единиц. Каждый символ - это какое-то число. Но из-за того, что мы знаем тип данных, то мы будем обращаться с этим числом как с символом.

Существуют специальные таблицы, в которых записано какому числу какой символ соответствует. В общем случае такая таблица будет называться кодировкой. Если нужно хранить только символы латинского алфавита, сойдет кодировка ASCII (в ней всего 255 символов). Однако если нужен, например, русский текст или эмодзи, то нужно использовать кодировку UTF-8.

Python по умолчанию использует кодировку UTF-8 (или unicode) для хранения строковых данных. Однако так было не всегда, это ввели только с 3 версии Python.

Часто при чтении файлов можно наблюдать вместо нужного текста какие-то странные символы. Скорее всего, файл прочитался не в той кодировке. В такой ситуации нужно уточнить кодировку файла и открыть его в нужной кодировке.

Чтобы создать строку, можно использовать одинарные или двойные кавычки (они равнозначны):

```python
'hello, world!' # это строка
"hello, world!" # и это строка

# если в тексте строки есть одинарная кавычка, то лучше для создания строки использовать двойные кавычки
"this text have ' and you must use another quote symbol"
```

Подробнее про этот тип данных поговорим позже в специальном уроке.

## Логический тип

Логический тип `bool` содержит всего два значения - `True` и `False`. Возникает при сравнении чисел, например

```python
10 < 15 # True
15 < 10 # False
```

Подробнее про этот тип данных поговорим в уроке про ветвление и условный оператор if.

## Тип None

Иногда нам нужно хранить пустое значение (чтобы позже записать сюда что-то полезное). Для таких случаев полезен тип `None`. С этим типом нельзя делать никакие операции и он ничего не означает. Мы его используем, чтобы как-то описать пустое значение.

Позже при решении задач мы еще не раз столкнемся с ним.

## Подведем итог

Благодаря типам данных Python понимает как обрабатывать данные в какой-то ячейке памяти. Если это число, он их обработает как число. Если это логический тип, то как логический тип.

Для удобства объединим все типы данных в одну таблицу:

| Тип данных | Название в Python | Пример |
| ---------- | ----------------- | ------ |
| Целые числа | int | 0, 1, -1, 100 |
| Вещественные числа | float | 0.1, 1.0, 0.12345 |
| Строки | str | 'hello, world!', "123" |
| Логический тип | bool | True, False |
| Пустой тип | None | None |

Не нужно учить эту таблицу наизусть, достаточно просто вернуться к ней, если будет что-то непонятно в будущем. Типы данных запомнятся только при практике решения задач.

## Переменные

Итак, мы поняли как именно обрабатывать данные разных типов. Но как сохранить какое-то значение в память? В этом нам помогут переменные.

Переменная - это ссылка на область в памяти, в которой хранится какое-то значение. У переменной есть имя и значение.

Давайте посмотрим на примере:

```python
a = 1
b = 5.2
c = 'some string'
d = True
```

Мы только что создали 4 переменные - `a`, `b`, `c` и `d`. Имена для переменных мы задаем сами, а тип определяется автоматически. После этой записи Python поймет, например, что в переменной с именем `a` лежит целое число `1`, сам выделит память под это число, сохранит его и при обращении к этому числу будет знать откуда взять значение.

Переменную можно себе представлять как коробочку. На коробочке есть надпись (ее имя), а также внутри нее есть какое-то содержимое (значение). Коробки бывают разных цветов (типов данных), и мы знаем, что внутри красных коробочек всегда лежат целые числа, а внутри зеленых - строки. Python позволяет сохранять нам миллионы таких коробочек в оперативной памяти и удобно работать с ними.

Чтобы проверить какому типу данных принадлежит переменная, можно использовать функцию `type`

```python
type(a) # int
```

## Статически и динамически типизированные языки программирования

Как уже было сказано выше, Python автоматически понимает какому типу данных принадлежит переменная в каждый момент времени. Например, мы можем сначала положить целочисленное значение в переменную, а потом в эту же переменную записать строку вместо старого значения и Python нас поймет:

```python
# записали int
a = 1
type(a) # int

# записали str, старое значение стерлось
a = '1'
type(a) # тип поменялся, уже str
```

Python не связывает переменную с ее типом данных и знает тип переменной только в момент, когда к ней обращаются. Так происходит из-за того, что Python - язык программирования с динамической типизацией. Как альтернатива существуют языки программирования со статической типизацией (например, C++, Java, C#). В них у каждой переменной должен быть указан тип и он не может меняться в течение исполнения программы.

С одной стороны динамическая типизация выигрывает из-за того, что это банально удобнее писать и проще читать. Сравните два кусочка кода:

```python
a = 1
a = str(a)
```

```java
int a = 1
String b = a.toString()
```

Но есть и довольно серьезные минусы. Например, на проверку типов тратится довольно много времени и это одна из причин почему Python медленный язык программирования.

Изменения последних нескольких версий Python (3.9, 3.10, 3.11) были направлены на улучшение системы типов языка.

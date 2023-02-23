1. Переменная x имеет тип numpy.array, что вернет x[x > 3] ?

- Элементы массива с индексом больше 3
- элементы массива с индексом больше 2
- Элементы исходного массива, значения которых больше 3, в той же последовательности, в которой они встречались в массиве  **this**
- Элементы исходного массива, значения которых больше 3, в произвольном порядке

2. Выберите все верные утверждения.

- numpy.random.rand(4, 5) вернет двумерный массив размером 4 на 5.  **this**
- numpy.random.rand(4, 5) вернет случайное число от 4 до 5.
- numpy.arange работает существенно быстрее range при генерации коллекций большого размера. **this**
- Если x имеет тип numpy.ndarray, выражение x * 5 вернет массив, состоящий из повторенного 5 раз x.

3. Объект frame имеет тип pandas.DataFrame. Какая из предложенных команд позволяет получить размер объекта frame в строках и столбцах?

- frame.size()
- frame.shape   **this**
- frame.shape()
- frame.size

4. Объект frame имеет тип pandas.DataFrame():

<table><tbody><tr><td><p></p></td><td><p>Name</p></td><td><p>Birth</p></td></tr><tr><td><p>1</p></td><td><p>Михаил Зайцев</p></td><td><p>22.04.1976</p></td></tr><tr><td><p>2</p></td><td><p>Максим Королёв</p></td><td><p>08.12.1993</p></td></tr></tbody></table>

Выберите команды, которые позволяют добавить в frame новый столбец под названием IsStudent так, чтобы после добавления столбца получившийся объект frame выглядел следующим образом:

<table><tbody><tr><td><p></p></td><td><p>Name</p></td><td><p>Birth</p></td><td><p>IsStudent</p></td></tr><tr><td><p>1</p></td><td><p>Михаил Зайцев</p></td><td><p>22.04.1976</p></td><td><p>False</p></td></tr><tr><td><p>2</p></td><td><p>Максим Королёв</p></td><td><p>08.12.1993</p></td><td><p>True</p></td></tr></tbody></table>

Примечание. В python несколько выражений, записанных через запятую и стоящих после "=" или "return", считаются кортежем (tuple). ***

- frame.addColumn('IsStudent', [False, True])
- frame['IsStudent'] = [False, True]    **this**
- frame['IsStudent'] = False, True      **this**
- frame['IsStudent'] = False and True
- frame['IsStudent'] = (False, True)    **this**
- frame['IsStudent'] = False True


# Ансамбли моделей

Мы уже видели, что у каждой модели есть какие-то свои недостатки и часто модели могут давать противоположные результаты. А что если мы построим не одну модель, а несколько и потом каким-то образом объединим эти предсказания? Такой подход называется построением ансамблей моделей. Существует несколько основных способов комбинирования моделей:

- Бэггинг - мы строим множество одинаковых алгоритмов и специально недообучаем их за счет того, что обучаемся на случайных подвыборках меньшего размера, а затем голосованием определяем ответ. Чаще всего этот метод используют для решающих деревьев и такой метод называют **случайный лес**;
- Бустинг - мы строим множество одинаковых алгоритмов, причем каждый следующий алгоритм учитывает ошибки предыдущего и стремится их уменьшить. В случае с бутстрапом мы можем обучать параллельно множество моделей, в случае с бустингом так не получится. Самый известный алгоритм - **градиентный бустинг**;
- Стекинг - мы строим множество различных алгоритмов, а затем обучаем финальный алгоритм, который обучается на ответах моделей и выносит свой вердикт.

## Случайный лес

Построим ансамбль алгоритмов, где базовый алгоритм — это решающее дерево. Будем строить по следующей схеме:

1. Для построения $i$-го дерева:
    1. Сначала из обучающей выборки $X$ выбирается с возвращением случайная подвыборка $X^i$ того же размера. (Такой метод называется **беггинг**)
    1. Затем случайно выбираются $n < N$ признаков, где $N$ — полное число признаков (**метод случайных подпространств**). Так же, как и подвыборка для каждого дерева, набор признаков свой для каждого из деревьев. Такой приём как раз позволяет управлять степенью скоррелированности базовых алгоритмов.
    1. На $n$ выбранных признаках подвыборки $X^i$ строится $i$-е дерево.
2. Чтобы получить предсказание ансамбля на тестовом объекте, усредняем отдельные ответы деревьев (для регрессии) или берём самый популярный класс (для классификации).
3. Profit. Мы построили **Random Forest (случайный лес)** – комбинацию бэггинга и метода случайных подпространств над решающими деревьями.

**Примечание:**

- random forest в sklearn усредняет вероятностные прогнозы классификаторов и на основании этого выбирает итоговый ответ, вместо того что бы выбирать наиболее популярный.
- random forest в sklearn выбирает случайное подпространство для каждого сплита дерева
- в sklearn по умолчанию деревья строятся максимальной глубины. Если вы не хотите, чтобы вашу память забили неприлично огромные деревья, ограничьте максимальную высоту каким-то большим, но при этом приемлимым по памяти и времени обучения значением

Построение леса:

![Forest1.png](attachment:Forest1.png)

Применение леса:

![Forest2.png](attachment:Forest2.png)

Основные аргументы:

- `n_estimators` - максимальное число деревьев в лесу
- `criterion` - критерий для создания узла: или критерий Джини gini (по умолчанию), или энтропия entropy.
- `max_depth` - максимальная глубина дерева
- `max_features` - максимальное число атрибутов, которые будут проверены при создании узла, по умолчанию это равно корню квадратному из числа всех атрибутов в данных.
- `max_samples` - максимальное число примеров используемых для одного дерева (примеры выбираются случайно).

Сам объект RandomForestClassifier имеет поля:

- `estimators_` - список объектов деревьев (типа DecisionTreeClassifier) в этом лесу
- `classes_` - метки классов
- `n_classes_` - число классов
- `n_features_` - число атрибутов
- `n_outputs_` - число выходов
- `feature_importances_` - оценка важности атрибутов. Очень полезные сведения, показывающие какой вклад дает тот или иной атрибут в точность решения задачи. Полезно, например, для существенного уменьшения размера дерева: удалив атрибуты с малой важностью не сильно потеряем в точности. Полезно и для интерпретируемости результатов. Вычисляется как суммарная величина уменьшения критерия неопределенности для этого атрибута./

Практические советы

- используем глубокие деревья. Но стоит ограничить глубину, поскольку по умолчанию деревья строяться максимально глубокими, а это может быть неэффективно по памяти.
- Используем $log_2(n)$ или $sqrt(n)$ признаков для дерева.
- Чем больше деревьев, тем лучше. Ограничить можно либо по времени работы, либо если функционал ошибки не уменьшается с ростом деревьев.

## Градиентный бустинг

Бустинг, использующий деревья решений в качестве базовых алгоритмов, называется градиентным бустингом над решающими деревьями, Gradient Boosting on Decision Trees, GBDT. Он отлично работает на выборках с «табличными», неоднородными данными. Бустинг способен эффективно находить нелинейные зависимости в данных различной природы. Этим свойством обладают все алгоритмы, использующие деревья решений, однако именно GBDT обычно выигрывает в подавляющем большинстве задач.

Не так хорошо бустинг проявляет себя на однородных данных: текстах, изображениях, звуке, видео. В таких задачах нейросетевые подходы почти всегда демонстрируют лучшее качество.

Хотя деревья решений и являются традиционным выбором для объединения в ансамбли, никто не запрещает использовать и другие алгоритмы, например, линейные модели в качестве базовых (эта возможность реализована в пакете XGBoost). Стоит только понимать, что построенная композиция по сути окажется линейной комбинацией линейных моделей, то есть опять-таки линейной моделью (или нейросетью с одним полносвязным слоем). Это уменьшает возможности ансамбля эффективно определять нелинейные зависимости в данных. В рамках данной главы мы будем рассматривать только бустинг над решающими деревьями.

### Алгоритм построения бустинга

Давайте разберем простой пример того, как может быть устроен бустинг для задачи регрессии. Допустим, мы хотим минимизировать среднеквадратичную ошибку.

$$\operatorname{MSE}(a, X)=\frac{1}{\ell} \sum_{i=1}^{\ell}\left(a\left(x_{i}\right)-y_{i}\right)^{2}$$

Начнем с того, что обучим один алгоритм, который будет решать нашу задачу, минимизировать среднеквадратичную ошибку. Это очень простая задача, мы умеем ее решать, например, градиентным спуском.

$$b_{1}(x)=\underset{b}{\operatorname{argmin}} \frac{1}{\ell} \sum_{i=1}^{\ell}\left(b\left(x_{i}\right)-y_{i}\right)^{2}$$

Хорошо. Итак, допустим, мы нашли $b_1$ — алгоритм из некого семейства алгоритмов, например, из семейства неглубоких решающих деревьев, который решает данную задачу. После этого мы можем нарисовать такую таблицу.

| Ответы        | Прогнозы      |
| ------------- |:-------------:|
| $b_1(x_1)$     | $y_1$ |
| $b_1(x_2)$      | $y_2$      |
| ...      | ...      |
| $b_1(x_l)$ | $y_l$      |

Теперь мы хотим добавить в композицию еще один алгоритм $b_2$. И возникает вопрос: а какие же ответы $b_2$ должен давать на объектах обучающей выборки, чтобы ошибка нашей композиции была как можно меньше? В общем-то, если записать уравнение

$$b_1(x_i) + b_2(x_i) = y_i$$

Из него легко понять, чему должен быть равен $b_2(x_i)$, чтобы давать наилучшее приближение к истинным ответам. $b_2(x_i)$ должен быть равен $y_i − b_1(x_i)$.

![boosting.png](attachment:boosting.png)

Тогда, если мы прибавим ответ нашего второго алгоритма к ответу первого алгоритма, то ответ $b_1 (x_i)$ сократится, и останется только $y_i$. То есть после прибавления $b_2$ к $b_1$ мы получим на объектах обучающей выборки нулевую ошибку, получим идеальные ответы.

Давайте тогда обучать $b_2$ так, чтобы его прогнозы были как можно ближе вот к этому вектору сдвигов, этому вектору ошибок. Получаем задачу, где минимизируется среднеквадратичное отклонение $b (x_i)$ от вот этих самых ошибок $y_i − b_1 (x_i)$.

$$b_{2}(x)=\underset{b}{\operatorname{argmin}} \frac{1}{\ell} \sum_{i=1}^{\ell}\left(b\left(x_{i}\right)-\left(y_{i}-b_{1}\left(x_{i}\right)\right)\right)^{2}$$

Если удастся решить задачу точно, то есть получить нулевую ошибку, то и наша композиция после добавления этого алгоритма b2 будет иметь нулевую ошибку. Но поскольку у нас алгоритмы базовые очень простые, скорее всего, точно решить задачу не получится, и поэтому b2 будет просто чуть-чуть улучшать качество первого базового алгоритма.

Этот процесс можно продолжать очень долго. $n$-ный базовый алгоритм мы будем настраивать на ошибку композиции из $(n − 1)$ алгоритма. Мы будем продолжать этот процесс до тех пор, пока ошибка на обучающей выборке не будет нас устраивать.

## Алгоритм работы градиентного бустинга

Будем строить композиции вот такого вида:

$$a_N(x) = \sum_{n=1}^N b_n(x)$$

Саму композицию из $N$ алгоритмов будем обозначать как $a_N(x)$ и она будет представлять собой сумму $N$ базовых алгоритмов $b_n (x)$. Обратите внимание, что мы не усредняем, а просто складываем базовые алгоритмы поскольку каждый следующий корректирует ошибки предыдущих.

Будем считать, что у нас есть некая функция потерь, которую мы хотим минимизировать. Функция потерь — это некая функция L, которая измеряет ошибку на одном объекте.

$$L(y, z)$$

Ее аргументами являются $y$, истинный ответ на этом объекте, и $z$, прогноз нашего алгоритма на этом объекте.

Первым шагом в построении бустинга является инициализация композиции каким-то простым алгоритмом. Например

- $b_0(x) = 0$
- $b_0(x) = \frac{1}{l}\sum_{i=1}^ly_i$
- $b_{0}(x)=\underset{y \in \mathbb{Y}}{\operatorname{argmax}} \sum_{i=1}^{\ell}\left[y_{i}=y\right]$

Далее действуем по индукции. Допустим мы уже построили:
$$a_{N-1}(x)=\sum_{n=0}^{N-1} b_{n}(x)$$

Попробуем понять, как именно нужно выбрать следующий базовый алгоритм $b_N$

Задача выглядит так:

$$\sum_{i=1}^{\ell} L\left(y_{i}, a_{N-1}\left(x_{i}\right)+b\left(x_{i}\right)\right) \rightarrow \min _{b}$$

Мы суммируем потери на всей обучающей выборке от уже построенной композиции $a(N – 1)$ и нового алгоритма $b (x)$. И будем пытаться выбрать алгоритм $b (x)$ так, чтобы как можно сильнее уменьшить ошибку композиции на обучающей выборке, то есть, чтобы как можно сильнее уменьшить функционал.

Для начала упростим себе задачу и попробуем ответить на более простой вопрос, а именно: какие значения наш новый базовый алгоритм должен принимать на объектах обучающей выборки, чтобы как можно сильнее уменьшить ошибку на обучающей выборке? Задача будет выглядеть вот так.

$$\sum_{i=1}^{\ell} L\left(y_{i}, a_{N-1}\left(x_{i}\right)+s_{i}\right) \rightarrow \min _{s_{1}, \ldots, s_{\ell}}$$

Мы суммируем функцию потерь по всем объектам из обучения и подставляем в нее следующий прогноз. Прогноз уже построенной композиции $N – 1$, и некоторый сдвиг этого прогноза на i-ом объекте, который мы будет обозначать, как $s_i$, и нужно найти такие значения $s_i$, чтобы они как можно сильнее уменьшили значение ошибки.

Мы получаем следующую задачу оптимизации:
$$F(s)=\sum_{i=1}^{\ell} L\left(y_{i}, a_{N-1}\left(x_{i}\right)+s_{i}\right) \rightarrow \min_{s}$$
$s = (s_1, ..., s_l)$ - вектор сдвигов

Нам нужно найти такой вектор сдвигов s, который будет минимизировать данную функцию $F (s)$. Вектор, который как можно сильнее уменьшает функцию — это антиградиент, поскольку он направлен в сторону наискорейшего убывания функции. Значит, вектор $s$ должен быть просто равен антиградиенту функции $F$, а именно он будет выглядеть вот так.

$$s=-\nabla F=(-L_{z}^{\prime}\left(y_{1}, a_{N-1}\left(x_{1}\right)\right), \ldots , -L_{z}^{\prime}\left(y_{l}, a_{N-1}\left(x_{l}\right)\right))$$

У него будет компонент столько, сколько объектов у нас на обучающей выборке и, например, первая компонента, это будет частная производная функции потерь $L$ по второму аргументу, по прогнозу, и вычислять мы ее будем в точке, которая равна прогнозу уже построенной композиции на объекте $x_1$, и все это берется с минусом.

Итак, мы поняли, как именно нужно сдвинуть прогнозы уже построенной композиции, чтобы достаточно хорошо уменьшить значение функции потерь на обучающей выборке. Иными словами, мы знаем какие значения новый алгоритм должен принимать на объектах обучающей выборки, и по этим значениям, в конечном числе точек, мы должны построить функцию $b (x)$, которая будет выдавать прогноз на любой точке из нашего пространства объектов.

$$b_{N}(x)=\underset{b}{\operatorname{argmin}} \frac{1}{\ell} \sum_{i=1}^{\ell}\left(b\left(x_{i}\right)-s_{i}\right)^{2}$$

- Вся информация о функции потерь L уже содержится в сдвигах $s_i$
- Используем MSE независимо от исходной задачи

**Примечание**: градиентный бустинг является универсальным апроксиматором только с условием неограниченной глубины

### Подведем итог

1. Строим начальный алгоритм $b_0(x)$
2. Для $n = 1,..., N$
   - Вычисляем сдвиги:
   $$s=(-L_{z}^{\prime}\left(y_{1}, a_{N-1}\left(x_{1}\right)\right), \ldots , -L_{z}^{\prime}\left(y_{l}, a_{N-1}\left(x_{l}\right)\right))$$
   - Обучаем новый базовый алгоритм:
   $$b_{N}(x)=\underset{b}{\operatorname{argmin}} \frac{1}{\ell} \sum_{i=1}^{\ell}\left(b\left(x_{i}\right)-s_{i}\right)^{2}$$
   - Добавляем алгоритм в композицию:
   $$a_n(x) = \sum_{m=1}^n b_m(x)$$

### Плюсы и минусы бустинга

**Плюсы**

- Можно легко интерпретировать (в отличии от нейросетевых методов).
- Устойчивый метод, который легко ограничивает переобучение.
- Требует гораздо меньше памяти чем RF

**Минусы**

- чувствителен к выбросам, поскольку каждый классификатор обязан исправлять ошибки в предыдущих. Таким образом, метод слишком зависит от выбросов в данных.
- метод практически невозможно распараллелить. Это связано с тем, что каждый следующий эстиматор основывает свои корректировки на предыдущих предикторах, что затрудняет оптимизацию процедуры.

Обычно для градиентного бустинга используют следующие библиотеки:

- XGBoost
- CatBoost
- LightGBM

**добавить примеры кода**

## Стекинг

Когда модели совершают разные ошибки, можно обучить модель, которая, например, посчитает среднее прогнозов, либо каким-то еще способом скорректирует итоговый прогноз.

**добавить примеры кода**

## Подбор гиперпараметров

Все параметры в машинном обучении можно поделить на два типа - те, которые мы задаем вручную до начала обучения модели и на те, которые подбираются автоматически. Параметры, которые нужно задавать вручную, называют **гиперпараметраим**.

Например, к гиперпараметрам относят learning rate в градиентном спуске, метод регуляризации, критерий информативности, глубина дерева, а также саму модель или ансамбль моделей.

Так как эти параметры влияют на итоговое качество модели, то нам хотелось бы как-то подбирать эти параметры. Самое простое что можно сделать - для каждого из параметров задать его возможные значения и перебрать все комбинации таких признаков, сравнивая их по метрике на тестовой выборке. Ровно это позволяет делать `GridSearchCV`. 

**добавить код**

Метод называется "поиск по сетке", потому что задавая возможные значения параметров мы формируем сетку параметров. Например, если бы у нас было всего два параметра, и мы бы отрисовали на плоскости все возможные их варианты, то получили бы сетку двух параметров

**добавить картинку**

В sklearn также есть другой способ подбора гиперпараметров - `RandomSearchCV`. Этот метод перебирает не все возможные варианты, а случайную подвыборку, но делает это по-умному и в итоге значение метрики незначительно отличается от оптимального варианта

**добавить код**

## AutoML

Модели машинного обучения и признаки тоже могут быть гиперпараметрами. Давайте для начала разберемся с моделями.

По сути, если мы хотим обучить другую модель, то нам нужно просто использовать другой класс, не меняя другой код. Поэтому можно перебирать сразу множество моделей и их параметры, отбирая лучшу.

Далее - зачастую если добавить к модели произведение некоторых признаков, или применить логарифм к некоторым признакам, то можно улучшить общее качество. В качестве гиперпараметра можно использовать флаг, при истинном значении которого мы к выборке добавим столбец с прологарифмированным значением другой колонки.

Итого можно написать код, который будет подбирать оптимальную модель для классификации или регрессии. Обычно библиотеки, которые реализуют такой подход, называют AutoML-библиотеками. Самые известные - [H2O](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/intro.html) и [AutoKeras](https://autokeras.com/).

Основные плюсы такого подхода:

- Минимум кода
- Поиск зависимостей, которые человек может и не найти

Однако минусы зачастую перевешивают:

- Очень долгое обучение, так как модель обучается тысячи или даже миллионы раз на разных датасетах
- Перебор бесполезных наборов параметров, которые вручную мы бы не стали даже рассматривать
- Потеря интерпретируемости моделей

AutoML - относительно новая концепция и не стоит ее бояться, но стоит использовать с осторожностью. Также не стоит ожидать, что внедрение autoML кратно увеличит качество моделей. Также стоит очень четко понимать, что именно нужно от модели и что лежит у вас в данных, чтобы случайно не переобучиться.
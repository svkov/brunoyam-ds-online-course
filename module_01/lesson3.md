# Подготовка к работе

Для начала работы нам понадобится несколько инструментов, о которых пойдет речь ниже. Эта часть курса может показаться скучной, но ее необходимо пройти и проделать один раз, чтобы все заработало и можно было комфортно работать.

## Anaconda

[Anaconda](https://www.anaconda.com/) - это инструмент, который позволяет быстро настроить среду для работы с данными. Anaconda можно условно разделить на две части - пакетный менеджер и виртуальную среду.

Пакетный менеджер `conda` позволяет быстро устанавливать необходимые для работы библиотеки. Например, мы хотим установить библиотеку numpy, тогда достаточно ввести команду `conda install numpy`, чтобы произвести установку. О том как устанавливать библиотеки подробнее поговорим в видео.

Помимо `conda` существует другой пакетный менеджер, который встроен в Python - pip. Он тоже позволяет ставить библиотеки, поэтому где-то можно встретить установку библиотек через `pip install`, однако pip не решает конфликты в зависимостях, поэтому в некоторых случаях можно случайно "сломать" виртуальное окружение. В таком случае придется создать новое окружение и заново в него все установить в нужном порядке.

Виртуальные среды нужны для того, чтобы у нас была возможность работать над несколькими проектами независимо друг от друга. Давайте представим, что у нас есть проект A, где используется Python 3.8, а также есть более новый проект B, где используется Python 3.9. Логично положить эти проекты и все их зависимости в отдельные папки, чтобы избежать конфликтов. Ровно это и позволяют делать виртуальные окружения. Создавая виртуальное окружение, мы создаем папку, в которую установится нужна версия Python и все необходимые библиотеки. Далее мы сможем активировать нужное окружение и работать с ним как будто других виртуальных окружений не существует.

![virtual_env](../images/venv_pic.jpeg)

[Полезные команды для Anaconda](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Jupyter Notebook (JupyterLab)

Для того, чтобы интерактивно работать с кодом на Python мы будем использовать специальный инструмент - Jupyter Notebook. Это среда разработки, которая позволяет запускать код в отдельных ячейках. Более близко с Jupyter Notebook мы познакомимся далее в видео.

Небольшая историческая справка. Изначально инструмент назывался IPython. Его функционал был очень ограничен, но идея была та же. Затем появился Jupyter Notebook, который позволил работать с кодом из браузера, добавил поддержку плагинов и стал визуально приятнее и понятнее. Сейчас все используют JupyterLab, который еще мощнее и удобнее. Если встретите одно из этих названий - знайте, что подразумевается одно и то же. Обычно "ноутбуком" называют любой файл, который можно открыть и в Jupyter Notebook и в JupyterLab.

Формат "юпитеров" стал очень популярен с развитием data science и теперь имеет поддержку на многих сайтах. Например, если выложить свой ноутбук на GitHub, то можно будет посмотреть содержимое файла прямо на сайте (без возможности редактирования и запуска, конечно).